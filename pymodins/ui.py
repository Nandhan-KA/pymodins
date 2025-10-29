import sys
import threading
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog

# Reuse catalogs and helpers from the Windows installer using a file-based import to avoid
# package attribute shadowing of the name "installer" in __init__.
import os
import importlib.util
import webbrowser
import json
import urllib.request
import re
import shutil
import ctypes
import time

# Compatibility map of Python version -> { package_name(lower): pinned_version }
# Only affects the UI installer; CLI keeps existing behavior.
PY_VERSION_COMPAT = {
    '3.6': {
        'numpy': '1.19.5',
        'pandas': '1.1.5',
        'scipy': '1.5.4',
        'matplotlib': '3.3.4',
        'scikit-learn': '0.24.2',
        'opencv-python': '4.5.5.64',
        'pillow': '8.4.0',
        'tensorflow': '2.6.0',
        'torch': '1.8.1',
    },
    '3.7': {
        'numpy': '1.21.6',
        'pandas': '1.3.5',
        'scipy': '1.7.3',
        'matplotlib': '3.5.3',
        'scikit-learn': '1.0.2',
        'opencv-python': '4.6.0.66',
        'pillow': '9.0.1',
        'tensorflow': '2.10.1',
        'torch': '1.13.1',
    },
    '3.8': {
        'numpy': '1.24.4',
        'pandas': '2.0.3',
        'scipy': '1.10.1',
        'matplotlib': '3.7.3',
        'scikit-learn': '1.3.2',
        'opencv-python': '4.8.1.78',
        'pillow': '10.1.0',
        'tensorflow': '2.13.0',
        'torch': '2.1.2',
    },
    '3.9': {
        'numpy': '2.1.3',
        'pandas': '2.2.3',
        'scipy': '1.13.1',
        'matplotlib': '3.8.4',
        'scikit-learn': '1.5.2',
        'opencv-python': '4.10.0.84',
        'pillow': '10.4.0',
        'tensorflow': '2.15.1',
        'torch': '2.4.1',
    },
    '3.10': {
        'numpy': '2.1.3',
        'pandas': '2.2.3',
        'scipy': '1.13.1',
        'matplotlib': '3.9.2',
        'scikit-learn': '1.5.2',
        'opencv-python': '4.10.0.84',
        'pillow': '10.4.0',
        'tensorflow': '2.16.2',
        'torch': '2.4.1',
    },
    '3.11': {
        'numpy': '2.1.3',
        'pandas': '2.2.3',
        'scipy': '1.13.1',
        'matplotlib': '3.9.2',
        'scikit-learn': '1.5.2',
        'opencv-python': '4.10.0.84',
        'pillow': '10.4.0',
        'tensorflow': '2.17.0',
        'torch': '2.5.1',
    },
    '3.12': {
        'numpy': '2.1.3',
        'pandas': '2.2.3',
        'scipy': '1.13.1',
        'matplotlib': '3.9.2',
        'scikit-learn': '1.5.2',
        'opencv-python': '4.10.0.84',
        'pillow': '10.4.0',
        'tensorflow': '2.17.0',
        'torch': '2.5.1',
    },
    '3.13': {
        # Best-effort; many ecosystems are still rolling out wheels for 3.13.
        # We intentionally avoid pinning most packages here.
        'numpy': '2.1.3',
        'pandas': '2.2.3',
        'matplotlib': '3.9.2',
    },
}

PYPI_CACHE = {}

def normalize_pkg(name: str) -> str:
    return (name or '').strip().lower()

def _pypi_json_for(package: str):
    key = normalize_pkg(package)
    if key in PYPI_CACHE:
        return PYPI_CACHE[key]
    try:
        with urllib.request.urlopen(f"https://pypi.org/pypi/{package}/json", timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            PYPI_CACHE[key] = data
            return data
    except Exception:
        PYPI_CACHE[key] = None
        return None

def get_latest_compatible_version(package: str, py_version: str):
    """Best-effort: choose the newest version compatible with the selected Python version.
    We read PyPI JSON and inspect 'requires_python' markers of releases.
    Returns a version string or None if undetermined.
    """
    data = _pypi_json_for(package)
    if not data:
        return None
    releases = data.get('releases') or {}
    if not isinstance(releases, dict):
        return None
    # Collect versions sortable; filter by requires_python if present
    def is_compatible(files):
        # If any file has no requires_python, assume compatible; otherwise ensure py_version satisfies marker text simply.
        for f in files:
            rp = f.get('requires_python')
            if not rp:
                return True
            # Very light check: accept common forms like ">=3.8", ">=3.8,<3.12"
            text = rp.replace(" ", "")
            ok = True
            for clause in text.split(','):
                if clause.startswith(">="):
                    ok = ok and (py_version >= clause[2:])
                elif clause.startswith(">"):
                    ok = ok and (py_version > clause[1:])
                elif clause.startswith("<="):
                    ok = ok and (py_version <= clause[2:])
                elif clause.startswith("<"):
                    ok = ok and (py_version < clause[1:])
                elif clause.startswith("=="):
                    ok = ok and (py_version == clause[2:])
            if ok:
                return True
        return False
    # Sort versions via package order in JSON's 'releases' keys descending; fall back to 'info.version'
    candidates = []
    for ver, files in releases.items():
        if not files:
            continue
        if is_compatible(files):
            candidates.append(ver)
    if not candidates:
        return None
    try:
        # Attempt PEP 440 sort by using packaging if available; else fallback lexical which is usually fine for semver-like
        from packaging.version import parse as vparse
        candidates.sort(key=vparse, reverse=True)
    except Exception:
        candidates.sort(reverse=True)
    return candidates[0]

def resolve_requirement_for_version(module_name: str, py_version: str) -> str:
    """Return a pip requirement string for the given module and Python version.
    If a pinned version exists in PY_VERSION_COMPAT, append '==<ver>' else return the module as-is.
    Handles common name variants (e.g., pillow/Pillow).
    """
    base = normalize_pkg(module_name)
    # Map a few known aliases to their canonical pip names
    alias = {
        'pil': 'pillow',
        'pillow': 'pillow',
        'opencv': 'opencv-python',
        'opencv-python': 'opencv-python',
        'scikit learn': 'scikit-learn',
        'scikit-learn': 'scikit-learn',
    }
    canonical = alias.get(base, base)
    pinned = PY_VERSION_COMPAT.get(py_version, {}).get(canonical)
    if pinned:
        return f"{canonical}=={pinned}"
    # Dynamic fallback: query PyPI to choose a compatible version for any package
    ver = get_latest_compatible_version(canonical, py_version)
    if ver:
        return f"{canonical}=={ver}"
    return module_name

_installer_spec = importlib.util.spec_from_file_location(
    'pymodins_installer_mod',
    os.path.join(os.path.dirname(__file__), 'installer.py')
)
installer_mod = importlib.util.module_from_spec(_installer_spec)
assert _installer_spec and _installer_spec.loader
_installer_spec.loader.exec_module(installer_mod)

def get_modules_for_category(category_name):
    """Return the list of modules for a given human-readable category name.
    Mirrors the lookup used in installer.py using lower().replace(" ", "_") on the name.
    """
    var_name = category_name.lower().replace(" ", "_")
    return getattr(installer_mod, var_name, [])

def _dedupe_preserve_order(items):
    seen = set()
    out = []
    for x in items:
        if x and x.lower() not in seen:
            seen.add(x.lower())
            out.append(x)
    return out

def discover_python_scripts_folders():
    candidates = []
    # 1) Python launcher listings
    try:
        result = subprocess.run(["py", "-0p"], capture_output=True, text=True)
        if result.returncode == 0:
            for line in (result.stdout or '').splitlines():
                path = line.strip()
                if not path:
                    continue
                # path points to python.exe; Scripts likely in same dir
                parent = os.path.dirname(path)
                scripts = os.path.join(parent, 'Scripts')
                if os.path.isfile(os.path.join(scripts, 'pip.exe')):
                    candidates.append(scripts)
    except Exception:
        pass
    # 2) User install directory
    try:
        user_dir = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python")
        if os.path.isdir(user_dir):
            for name in os.listdir(user_dir):
                scripts = os.path.join(user_dir, name, 'Scripts')
                if os.path.isfile(os.path.join(scripts, 'pip.exe')):
                    candidates.append(scripts)
    except Exception:
        pass
    # 3) Program Files
    for base in [r"C:\\Program Files", r"C:\\Program Files (x86)"]:
        try:
            if os.path.isdir(base):
                for name in os.listdir(base):
                    if name.lower().startswith('python'):
                        scripts = os.path.join(base, name, 'Scripts')
                        if os.path.isfile(os.path.join(scripts, 'pip.exe')):
                            candidates.append(scripts)
        except Exception:
            pass
    # 4) Current interpreter prefixes
    for p in [sys.prefix, sys.base_prefix]:
        try:
            scripts = os.path.join(p, 'Scripts')
            if os.path.isfile(os.path.join(scripts, 'pip.exe')):
                candidates.append(scripts)
        except Exception:
            pass
    # 5) PATH entries
    try:
        for part in (os.environ.get('PATH') or '').split(';'):
            if not part:
                continue
            if os.path.basename(part).lower() == 'scripts' and os.path.isfile(os.path.join(part, 'pip.exe')):
                candidates.append(os.path.normpath(part))
    except Exception:
        pass
    return _dedupe_preserve_order(candidates)


class InstallerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PYMODINS - Windows UI")
        self.geometry("980x640")
        self.minsize(880, 560)

        self._install_in_progress = False
        self._selected_python_version = 'auto'
        self._selected_python_folder = None  # Root or Scripts folder
        # Color palette
        self.color_bg = "#ffffff"
        self.color_panel = "#f8f9fa"  # light gray
        self.color_text = "#212529"   # dark gray
        self.color_muted = "#6c757d"  # medium gray
        self.color_accent = "#007bff" # blue
        self.color_good = "#28a745"   # green
        self.color_warn = "#ffc107"   # yellow
        self.color_alert = "#dc3545"  # red
        self.configure(bg=self.color_bg)

        # Ensure Windows and admin preconditions
        if platform.system().lower() != "windows":
            messagebox.showerror("Unsupported Platform", "This UI is designed for Windows only.")
            self.after(100, self.destroy)
            return

        if not installer_mod.internet():
            messagebox.showwarning("No Internet", "An active internet connection is required.")

        if not installer_mod.is_admin():
            if messagebox.askyesno("Admin Required", "Administrative privileges are required for installations.\n\nElevate now?"):
                if installer_mod.run_as_admin():
                    # Relaunch will occur, exit current process
                    self.after(100, self.destroy)
                    return
                else:
                    messagebox.showerror("Elevation Failed", "Could not acquire administrative privileges.")

        self.apply_style()
        self.create_menu()
        self.create_widgets()
        self.populate_categories()

    def create_widgets(self):
        # Notebook for pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Install page
        install_page = ttk.Frame(self.notebook)
        self.notebook.add(install_page, text="Install")

        # Header (Install)
        header = ttk.Frame(install_page, padding=(10, 10))
        header.pack(fill=tk.X)
        ttk.Label(header, text="PYMODINS", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="Install curated Python modules with a click.", style="Subtitle.TLabel").pack(anchor="w")

        # Top controls (Install)
        top_frame = ttk.Frame(install_page, padding=(10, 6))
        top_frame.pack(fill=tk.X)
        self.btn_upgrade = ttk.Button(top_frame, text="Upgrade pip", command=self.on_upgrade_pip)
        self.btn_upgrade.pack(side=tk.LEFT)
        ttk.Button(top_frame, text="System Info", command=self.on_system_info).pack(side=tk.LEFT, padx=(10, 0))
        # Python version selector (UI-only behavior)
        ttk.Label(top_frame, text="Python version:").pack(side=tk.LEFT, padx=(16, 4))
        self.pyver_var = tk.StringVar(value='auto')
        self.pyver_combo = ttk.Combobox(
            top_frame,
            textvariable=self.pyver_var,
            state='readonly',
            values=['auto', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13']
        )
        self.pyver_combo.pack(side=tk.LEFT)
        self.pyver_combo.bind('<<ComboboxSelected>>', self.on_pyver_change)
        # Auto-discovered Python folders dropdown
        ttk.Label(top_frame, text="Python folder:").pack(side=tk.LEFT, padx=(16, 4))
        self.pyfolder_choice_var = tk.StringVar(value='auto')
        self.pyfolder_combo = ttk.Combobox(
            top_frame,
            textvariable=self.pyfolder_choice_var,
            state='readonly'
        )
        self.pyfolder_combo.pack(side=tk.LEFT)
        self.pyfolder_combo.bind('<<ComboboxSelected>>', self.on_pyfolder_change)

        # Main panes
        main_pane = ttk.PanedWindow(install_page, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Categories list
        left_frame = ttk.Frame(main_pane)
        ttk.Label(left_frame, text="Categories").pack(anchor="w")
        cat_wrap = ttk.Frame(left_frame)
        cat_wrap.pack(fill=tk.BOTH, expand=True)
        cat_scroll = ttk.Scrollbar(cat_wrap, orient=tk.VERTICAL)
        self.category_list = tk.Listbox(
            cat_wrap,
            height=20,
            exportselection=False,
            bg=self.color_panel,
            fg=self.color_text,
            selectbackground=self.color_accent,
            highlightthickness=0,
            activestyle='none',
            relief=tk.FLAT,
            font=('Segoe UI', 10)
        )
        self.category_list.configure(yscrollcommand=cat_scroll.set)
        cat_scroll.configure(command=self.category_list.yview)
        self.category_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        cat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.category_list.bind("<<ListboxSelect>>", self.on_category_select)
        main_pane.add(left_frame, weight=1)

        # Modules and actions
        right_frame = ttk.Frame(main_pane)
        ttk.Label(right_frame, text="Modules").pack(anchor="w")
        mod_wrap = ttk.Frame(right_frame)
        mod_wrap.pack(fill=tk.BOTH, expand=True)
        mod_scroll = ttk.Scrollbar(mod_wrap, orient=tk.VERTICAL)
        self.module_list = tk.Listbox(
            mod_wrap,
            selectmode=tk.EXTENDED,
            height=20,
            bg=self.color_panel,
            fg=self.color_text,
            selectbackground=self.color_accent,
            highlightthickness=0,
            activestyle='none',
            relief=tk.FLAT,
            font=('Segoe UI', 10)
        )
        self.module_list.configure(yscrollcommand=mod_scroll.set)
        mod_scroll.configure(command=self.module_list.yview)
        self.module_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        mod_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        btns = ttk.Frame(right_frame)
        btns.pack(fill=tk.X, pady=(8, 0))
        self.btn_install_sel = ttk.Button(btns, text="Install Selected", command=self.on_install_selected)
        self.btn_install_sel.pack(side=tk.LEFT)
        self.btn_install_all = ttk.Button(btns, text="Install All", command=self.on_install_all)
        self.btn_install_all.pack(side=tk.LEFT, padx=(10, 0))
        main_pane.add(right_frame, weight=2)

        # Log output (Install)
        log_container = ttk.Frame(install_page, padding=(10, 0))
        log_container.pack(fill=tk.BOTH, expand=True)
        progress_row = ttk.Frame(log_container)
        progress_row.pack(fill=tk.X, pady=(0, 6))
        self.progress = ttk.Progressbar(progress_row, mode='determinate')
        self.progress.pack(fill=tk.X, expand=True)
        log_frame = ttk.LabelFrame(log_container, text="Output")
        log_frame.pack(fill=tk.BOTH, expand=True)
        log_wrap = ttk.Frame(log_frame)
        log_wrap.pack(fill=tk.BOTH, expand=True)
        log_scroll = ttk.Scrollbar(log_wrap, orient=tk.VERTICAL)
        self.log_text = tk.Text(
            log_wrap,
            height=10,
            wrap=tk.WORD,
            bg=self.color_panel,
            fg=self.color_text,
            insertbackground=self.color_text,
            relief=tk.FLAT,
            font=('Consolas', 10)
        )
        self.log_text.configure(yscrollcommand=log_scroll.set)
        log_scroll.configure(command=self.log_text.yview)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        _init_log_tags(self.log_text)

        # Chat command bar
        chat = ttk.Frame(install_page, padding=(10, 6))
        chat.pack(fill=tk.X)
        ttk.Label(chat, text="Ask PYMODINS:").pack(side=tk.LEFT, padx=(0, 8))
        self.chat_var = tk.StringVar()
        self.chat_entry = ttk.Entry(chat, textvariable=self.chat_var, width=60)
        self.chat_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(chat, text="Go", command=self.on_chat_go).pack(side=tk.LEFT, padx=(8, 0))

        # System Info page
        sys_page = ttk.Frame(self.notebook)
        self.notebook.add(sys_page, text="System Info")

        sys_hdr = ttk.Frame(sys_page, padding=(10, 10))
        sys_hdr.pack(fill=tk.X)
        ttk.Label(sys_hdr, text="System Information", style="Title.TLabel").pack(anchor="w")
        ttk.Label(sys_hdr, text="Environment details detected by PYMODINS.", style="Subtitle.TLabel").pack(anchor="w")
        sys_controls = ttk.Frame(sys_page, padding=(10, 6))
        sys_controls.pack(fill=tk.X)
        ttk.Button(sys_controls, text="Refresh", command=self.render_system_info).pack(side=tk.LEFT)

        sys_body = ttk.Frame(sys_page, padding=(10, 6))
        sys_body.pack(fill=tk.BOTH, expand=True)
        self.sysinfo_tree = ttk.Treeview(sys_body, columns=("value",), show="tree")
        self.sysinfo_tree.pack(fill=tk.BOTH, expand=True)

        # Status bar
        status = ttk.Frame(self, padding=(10, 6))
        status.pack(fill=tk.X)
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(status, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w")
        
        # Initial system info render
        self.render_system_info()


    def create_menu(self):
        menubar = tk.Menu(self)
        app_menu = tk.Menu(menubar, tearoff=0)
        app_menu.add_command(label="Upgrade pip", command=self.on_upgrade_pip)
        app_menu.add_separator()
        app_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="App", menu=app_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
            "About PYMODINS",
            "PYMODINS UI\nCurated Python module installer for Windows by Nandhan K."
        ))
        help_menu.add_separator()
        help_menu.add_command(label="Documentation", command=lambda: webbrowser.open('https://pymodins.readthedocs.io/en/latest/'))
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def apply_style(self):
        style = ttk.Style()
        try:
            style.theme_use('vista')
        except Exception:
            pass
        # Base colors for light UI
        style.configure('TFrame', background=self.color_bg)
        style.configure('TLabelframe', background=self.color_bg, foreground=self.color_text)
        style.configure('TLabelframe.Label', background=self.color_bg, foreground=self.color_text)
        style.configure('TNotebook', background=self.color_bg, borderwidth=0)
        style.configure('TNotebook.Tab', background=self.color_panel, foreground=self.color_text, padding=(12, 6))
        style.map('TNotebook.Tab', background=[('selected', self.color_bg)], foreground=[('selected', self.color_text)])
        style.configure('TPanedwindow', background=self.color_bg)

        style.configure('Title.TLabel', font=('Segoe UI', 20, 'bold'), foreground=self.color_text, background=self.color_bg)
        style.configure('Subtitle.TLabel', font=('Segoe UI', 10), foreground=self.color_muted, background=self.color_bg)
        style.configure('Status.TLabel', font=('Segoe UI', 9), foreground=self.color_muted, background=self.color_bg)
        style.configure('TLabel', foreground=self.color_text, background=self.color_bg)
        style.configure('TButton', padding=6)
        style.map('TButton', foreground=[('disabled', self.color_muted)])

    def on_pyver_change(self, _event=None):
        sel = self.pyver_var.get().strip()
        self._selected_python_version = sel or 'auto'
        if self._selected_python_version != 'auto':
            self.status_var.set(f"Using Python {self._selected_python_version} compatibility for installs")
        else:
            self.status_var.set("Using current interpreter for installs")

    def on_select_python_folder(self):
        # Let user select a folder; accept either root (containing Scripts) or the Scripts folder itself
        folder = filedialog.askdirectory(title="Select Python folder or its Scripts folder")
        if not folder:
            return
        folder = os.path.normpath(folder)
        # Normalize to Scripts folder if root
        scripts = folder
        if os.path.basename(scripts).lower() != 'scripts':
            candidate = os.path.join(scripts, 'Scripts')
            if os.path.isdir(candidate):
                scripts = candidate
        pip_exe = os.path.join(scripts, 'pip.exe')
        if not os.path.isfile(pip_exe):
            messagebox.showerror("Invalid Folder", "Selected folder does not contain pip.exe (expected in a Scripts folder).")
            return
        self._selected_python_folder = scripts
        self.pyfolder_choice_var.set(scripts) # Set the combobox value
        self.status_var.set(f"Using selected Python folder for installs: {os.path.basename(os.path.dirname(scripts))}\\Scripts")

    def _resolve_pip_command(self, requirement: str):
        """Return (cmd_list, cwd, python_folder_for_log) using either selected Scripts pip.exe or current interpreter."""
        if self._selected_python_folder:
            pip_path = os.path.join(self._selected_python_folder, 'pip.exe')
            if os.path.isfile(pip_path):
                return ([pip_path, 'install', requirement], self._selected_python_folder, os.path.basename(os.path.dirname(self._selected_python_folder)))
        # Fallback to current interpreter
        return ([sys.executable, '-m', 'pip', 'install', requirement], None, 'current-interpreter')

    def populate_categories(self):
        # Use the same human-readable list from installer (skip the leading None)
        self.categories = [c for c in installer_mod.module_types if c]
        self.category_list.delete(0, tk.END)
        for c in self.categories:
            self.category_list.insert(tk.END, c)
        # Also populate Python folders after categories are ready (during init)
        self.populate_python_folders()

    def populate_python_folders(self):
        self._pyfolder_display_to_path = {'auto': None}
        display_values = ['auto']
        for scripts in discover_python_scripts_folders():
            # Display as <ParentName>\\Scripts (e.g., Python311\Scripts)
            parent = os.path.basename(os.path.dirname(scripts))
            display = f"{parent}\\Scripts"
            # Ensure unique display; if collision, append index
            orig_display = display
            idx = 2
            while display in self._pyfolder_display_to_path:
                display = f"{orig_display} ({idx})"
                idx += 1
            self._pyfolder_display_to_path[display] = scripts
            display_values.append(display)
        self.pyfolder_combo.configure(values=display_values)
        self.pyfolder_combo.set('auto')

    def on_pyfolder_change(self, _event=None):
        choice = self.pyfolder_choice_var.get().strip() or 'auto'
        path = self._pyfolder_display_to_path.get(choice)
        self._selected_python_folder = path
        if path:
            self.status_var.set("Using selected Python folder for installs")
        else:
            self.status_var.set("Using current interpreter for installs")

    def on_category_select(self, _event=None):
        sel = self.category_list.curselection()
        if not sel:
            return
        category = self.categories[sel[0]]
        modules = get_modules_for_category(category)
        self.module_list.delete(0, tk.END)
        for m in modules:
            self.module_list.insert(tk.END, m)

    def ensure_ready(self):
        if platform.system().lower() != "windows":
            messagebox.showerror("Unsupported Platform", "Windows only.")
            return False
        if not installer_mod.is_admin():
            messagebox.showerror("Admin Required", "Please run as Administrator and try again.")
            return False
        if not installer_mod.internet():
            messagebox.showerror("No Internet", "Please connect to the internet and try again.")
            return False
        return True

    def on_upgrade_pip(self):
        if not self.ensure_ready():
            return
        self.append_log("Upgrading pip...\n")
        threading.Thread(target=self._upgrade_pip_worker, daemon=True).start()

    def _upgrade_pip_worker(self):
        try:
            installer_mod.upgrade_pip()
            self.append_log("pip upgraded successfully.\n")
        except Exception as e:
            self.append_log(f"Failed to upgrade pip: {e}\n")

    def on_system_info(self):
        try:
            self.render_system_info()
            # Switch to System Info tab
            for i in range(self.notebook.index('end')):
                if self.notebook.tab(i, 'text') == 'System Info':
                    self.notebook.select(i)
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load system info: {e}")

    def render_system_info(self):
        # Populate the tree with key/value pairs
        self.sysinfo_tree.delete(*self.sysinfo_tree.get_children())
        def add(label, value):
            self.sysinfo_tree.insert('', 'end', text=f"{label}: {value}")
        try:
            add('System Platform', sys.platform)
            add('Python Version', sys.version.replace('\n', ' '))
            add('Executable', sys.executable)
            pip_version = subprocess.check_output(["pip", "--version"]).decode().strip()
            add('pip', pip_version)
            add('Admin', bool(installer_mod.is_admin()))
            add('Internet', bool(installer_mod.internet()))
            # CPU
            cpu_name = platform.processor() or 'Unknown CPU'
            cores = os.cpu_count() or 0
            add('CPU', f"{cpu_name} ({cores} cores)")
            # RAM
            total_ram, avail_ram = _get_windows_memory_gb()
            if total_ram is not None:
                add('Memory (RAM)', f"Total: {total_ram:.1f} GB, Available: {avail_ram:.1f} GB")
            else:
                add('Memory (RAM)', 'N/A')
            # Disk
            total_disk, used_disk, free_disk = _get_disk_usage_gb()
            if total_disk is not None:
                add('Disk (System Drive)', f"Total: {total_disk:.1f} GB, Free: {free_disk:.1f} GB")
            else:
                add('Disk (System Drive)', 'N/A')
            # Network speed placeholder
            self._net_speed_item = self.sysinfo_tree.insert('', 'end', text='Network Speed: estimating...')
            def _compute_speed():
                speed = _measure_network_speed_mb_s()
                text = f"Network Speed: {speed:.2f} MB/s" if speed is not None else 'Network Speed: N/A'
                try:
                    self.sysinfo_tree.item(self._net_speed_item, text=text)
                except Exception:
                    pass
            threading.Thread(target=_compute_speed, daemon=True).start()
        except Exception as e:
            add('Error', str(e))

    def on_install_selected(self):
        if not self.ensure_ready():
            return
        cat_sel = self.category_list.curselection()
        if not cat_sel:
            messagebox.showinfo("Select Category", "Please select a category.")
            return
        category = self.categories[cat_sel[0]]
        indices = self.module_list.curselection()
        if not indices:
            messagebox.showinfo("Select Modules", "Please select one or more modules to install.")
            return
        modules = [self.module_list.get(i) for i in indices]
        self._install_modules(category, modules)

    def on_install_all(self):
        if not self.ensure_ready():
            return
        cat_sel = self.category_list.curselection()
        if not cat_sel:
            messagebox.showinfo("Select Category", "Please select a category.")
            return
        category = self.categories[cat_sel[0]]
        modules = list(get_modules_for_category(category))
        if not modules:
            messagebox.showinfo("No Modules", "No modules found for this category.")
            return
        if not messagebox.askyesno("Confirm", f"Install all modules in '{category}'?\nThis may take a while."):
            return
        self._install_modules(category, modules)

    def _install_modules(self, category, modules):
        if self._install_in_progress:
            return
        self._install_in_progress = True
        self.set_controls_state("disabled")
        self.status_var.set("Installing packages...")
        self.progress.configure(maximum=len(modules), value=0)
        self.append_log(f"Category: {category}\n")
        self.append_log(f"Modules: {', '.join(modules)}\n")
        threading.Thread(target=self._install_worker, args=(category, modules), daemon=True).start()

    def _install_worker(self, category, modules):
        # Prefer current interpreter; this avoids brittle path guessing.
        completed = 0
        for module in modules:
            norm = normalize_pkg(module)
            # Special-case handling before computing requirement
            if norm == 'rust':
                self.append_log("Installing Rust toolchain via system installer...\n")
                try:
                    ok = installer_mod.install_rust()
                    if ok:
                        self.append_log("✓ Rust installed successfully.\n")
                        try:
                            installer_mod.log_mod(category, 'rust', python_folder='system')
                        except Exception:
                            pass
                    else:
                        self.append_log("✗ Rust installation reported failure.\n")
                except Exception as e:
                    self.append_log(f"Error installing Rust: {e}\n")
                finally:
                    completed += 1
                    self.update_progress_safe(completed)
                continue
            if norm == 'dlib':
                # Ensure VS Build Tools before attempting pip install of dlib
                self.append_log("Preparing environment for dlib (installing Visual Studio Build Tools if needed)...\n")
                try:
                    if messagebox.askyesno(
                        "Visual Studio Build Tools",
                        "Installing Visual Studio Build Tools may take a minimum of 10 minutes\n"
                        "and requires at least 1.25 GB of data.\n\nDo you want to continue?"
                    ):
                        installer_mod.install_vscode_build_tools()
                        self.append_log("VS Build Tools install invoked. Proceeding with dlib.\n")
                    else:
                        self.append_log("Skipped VS Build Tools installation as requested. dlib may fail to build.\n")
                except Exception as e:
                    self.append_log(f"Warning: Failed to invoke VS Build Tools installer: {e}\n")
            pyver = self._selected_python_version
            if pyver == 'auto':
                # Auto mode: use current interpreter without pinning (as before)
                requirement = module
                ver_note = f" (auto: {platform.python_version()})"
            else:
                requirement = resolve_requirement_for_version(module, pyver)
                ver_note = f" (using compat for Python {pyver})"
            self.append_log(f"Installing {requirement}{ver_note}...\n")
            try:
                cmd, cwd, py_folder_log = self._resolve_pip_command(requirement)
                rc = self._run_and_stream(cmd, cwd=cwd)
                if rc == 0:
                    self.append_log(f"✓ {requirement} installed.\n")
                    try:
                        # Log via existing helper
                        installer_mod.log_mod(category, requirement, python_folder=py_folder_log)
                    except TypeError:
                        # Older signature without python_folder
                        try:
                            installer_mod.log_mod(category, requirement)  # type: ignore
                        except Exception:
                            pass
                else:
                    self.append_log(f"✗ {requirement} failed ({rc}).\n")
            except Exception as e:
                self.append_log(f"Error installing {requirement}: {e}\n")
            finally:
                completed += 1
                self.update_progress_safe(completed)
        self.append_log("Done.\n")
        self.status_var.set("Ready")
        self.set_controls_state("!disabled")
        self._install_in_progress = False

    def append_log(self, text):
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)

    def update_progress_safe(self, value):
        try:
            self.progress['value'] = value
        except Exception:
            pass

    def set_controls_state(self, state):
        try:
            self.btn_upgrade.state([state])
            self.btn_install_sel.state([state])
            self.btn_install_all.state([state])
        except Exception:
            pass

    def on_chat_go(self):
        query = (self.chat_var.get() or '').strip().lower()
        if not query:
            return
        # Keyword to category mapping
        mapping = {
            'basic': 'Basic Modules',
            'beginner': 'Basic Modules',
            'advanced': 'Advanced Modules',
            'science': 'Science Modules',
            'computer vision': 'Computer Vision Modules',
            'vision': 'Computer Vision Modules',
            'ml': 'Machine Learning Modules',
            'machine learning': 'Machine Learning Modules',
            'deep learning': 'Deep Learning Modules',
            'dl': 'Deep Learning Modules',
            'full stack': 'Full Stack Development Modules',
            'network': 'Network Modules',
            'build': 'Build Modules',
            'jupyter': 'Jupyter Modules',
            'visualization': 'Data Visualization Modules',
            'data viz': 'Data Visualization Modules',
            'database': 'Database Modules',
            'cyber': 'Cybersecurity Modules',
            'security': 'Cybersecurity Modules',
            'cloud': 'Cloud Computing Modules',
            'devops': 'DevOps Modules',
            'big data': 'Big Data Modules',
        }
        target = None
        for key, cat in mapping.items():
            if key in query:
                target = cat
                break
        if not target:
            # Fallback: try to fuzzy match by words present in module_types
            for cat in installer_mod.module_types:
                if not cat:
                    continue
                if any(word in cat.lower() for word in query.split()):
                    target = cat
                    break
        if target:
            # Select category in listbox
            try:
                idx = self.categories.index(target)
                self.category_list.selection_clear(0, tk.END)
                self.category_list.selection_set(idx)
                self.category_list.see(idx)
                self.on_category_select(None)
                self.status_var.set(f"Selected: {target}")
            except ValueError:
                messagebox.showinfo("Not Found", f"No category matched: {target}")
        else:
            messagebox.showinfo("No Match", "Could not understand the request. Try including keywords like 'machine learning', 'vision', 'database', etc.")

    def _run_and_stream(self, cmd, cwd=None):
        try:
            proc = subprocess.Popen(
                cmd,
                cwd=cwd or None,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
            )
        except Exception as e:
            self.append_log(f"Failed to start process: {e}\n")
            return 1
        state = AnsiState()
        # Read line by line to keep UI responsive
        try:
            for line in iter(proc.stdout.readline, ''):
                try:
                    insert_ansi(self.log_text, line, state)
                except Exception:
                    # Fallback: plain append
                    self.append_log(line)
            proc.stdout.close()
        except Exception:
            pass
        return proc.wait()


def main():
    app = InstallerUI()
    # If platform/admin checks destroyed the window, avoid mainloop
    try:
        app.mainloop()
    except Exception:
        pass


def _init_log_tags(text_widget: tk.Text):
    # Basic foreground colors and styles to approximate terminal output
    colors = {
        'fg_black': '#000000', 'fg_red': '#d32f2f', 'fg_green': '#388e3c', 'fg_yellow': '#fbc02d',
        'fg_blue': '#1976d2', 'fg_magenta': '#7b1fa2', 'fg_cyan': '#0097a7', 'fg_white': '#e0e0e0',
        'fg_bright_black': '#616161', 'fg_bright_red': '#ff5252', 'fg_bright_green': '#69f0ae',
        'fg_bright_yellow': '#ffff00', 'fg_bright_blue': '#448aff', 'fg_bright_magenta': '#e040fb',
        'fg_bright_cyan': '#18ffff', 'fg_bright_white': '#ffffff'
    }
    for name, col in colors.items():
        text_widget.tag_configure(name, foreground=col)
    text_widget.tag_configure('bold', font=('Consolas', 10, 'bold'))

ANSI_RE = re.compile(r"\x1b\[(?P<codes>[0-9;]*)m")

SGR_TO_TAG = {
    0: 'reset',
    1: 'bold',
    30: 'fg_black', 31: 'fg_red', 32: 'fg_green', 33: 'fg_yellow', 34: 'fg_blue', 35: 'fg_magenta', 36: 'fg_cyan', 37: 'fg_white',
    90: 'fg_bright_black', 91: 'fg_bright_red', 92: 'fg_bright_green', 93: 'fg_bright_yellow', 94: 'fg_bright_blue', 95: 'fg_bright_magenta', 96: 'fg_bright_cyan', 97: 'fg_bright_white',
}

class AnsiState:
    def __init__(self):
        self.tags = []  # active tag names
    def reset(self):
        self.tags = []
    def apply_codes(self, codes):
        if not codes:
            self.reset()
            return
        for c in codes:
            tag = SGR_TO_TAG.get(c)
            if tag == 'reset':
                self.reset()
            elif tag:
                # ensure only one fg color active at once
                if tag.startswith('fg_'):
                    self.tags = [t for t in self.tags if not t.startswith('fg_')]
                if tag not in self.tags:
                    self.tags.append(tag)

def insert_ansi(text_widget: tk.Text, s: str, state: AnsiState):
    pos = 0
    for m in ANSI_RE.finditer(s):
        if m.start() > pos:
            seg = s[pos:m.start()]
            text_widget.insert(tk.END, seg, tuple(state.tags))
        code_str = m.group('codes')
        codes = [int(x) for x in code_str.split(';') if x.isdigit()] if code_str else []
        if not codes:
            codes = [0]
        state.apply_codes(codes)
        pos = m.end()
    if pos < len(s):
        text_widget.insert(tk.END, s[pos:], tuple(state.tags))
    text_widget.see(tk.END)

def _get_windows_memory_gb():
    try:
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]
        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
        total_gb = stat.ullTotalPhys / (1024**3)
        avail_gb = stat.ullAvailPhys / (1024**3)
        return total_gb, avail_gb
    except Exception:
        return None, None

def _get_disk_usage_gb():
    try:
        root = os.environ.get('SystemDrive', 'C:') + "\\"
        total, used, free = shutil.disk_usage(root)
        return total/(1024**3), used/(1024**3), free/(1024**3)
    except Exception:
        return None, None, None

def _measure_network_speed_mb_s(timeout_sec=6):
    # Best-effort: download ~1MB and time it
    url = 'https://speed.hetzner.de/1MB.bin'
    start = time.time()
    bytes_read = 0
    try:
        with urllib.request.urlopen(url, timeout=timeout_sec) as resp:
            while True:
                chunk = resp.read(64 * 1024)
                if not chunk:
                    break
                bytes_read += len(chunk)
                if time.time() - start > timeout_sec:
                    break
        elapsed = max(0.001, time.time() - start)
        mbps = (bytes_read / (1024*1024)) / elapsed
        return mbps
    except Exception:
        return None


