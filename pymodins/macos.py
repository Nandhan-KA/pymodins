import os
import getpass
import sys
import pip
import time
import urllib.request
from datetime import datetime
import subprocess
import webbrowser
from rich.console import Console
from rich.prompt import Prompt

console = Console()
user = subprocess.run(['whoami'], capture_output=True, text=True).stdout.strip()


def banner():
    console = Console()
    ascii_art = r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v3.3 macOS               
    """
    console.print(ascii_art, style="bold yellow")
    console.print("Creator: Nandhan K", style="bold cyan")
    console.print("Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\n For more info contact: developer.nandhank@gmail.com", style="bold green")


def banner_assist():
    console = Console()
    ascii_art = r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 Assistant@V1.0               
    """
    console.print(ascii_art, style="bold yellow")
    console.print("Creator: Nandhan K", style="bold cyan")
    console.print("Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("Pymodins Virtual Assistant for macOS")


def banner_nointernet():
    console = Console()
    ascii_art = r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v3.3 macOS                
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print(" \n \t This Project Requires Internet Connection 🌐 ", style="bold yellow")
    console.print("\n For more info contact: developer.nandhank@gmail.com", style="bold green")


def creator():
    console = Console()
    ascii_art = r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                v3.3 macOS                
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\n For more info contact: developer.nandhank@gmail.com", style="bold green")


def sys_info():
    console = Console()
    console.print(f"System Platform: {sys.platform}", style="bold white")
    console.print(f"Python version: {sys.version}", style="bold white")
    try:
        pip_version = subprocess.check_output(['pip3', '--version']).decode().strip()
        console.print(f"pip version: {pip_version}", style="bold white")
        console.print(f"User: {user}", style="bold white")
        console.print(f"Homebrew installed: {is_homebrew_installed()}", style="bold white")
    except Exception as e:
        console.print(f"Error: {e}. Ensure Python and pip are properly installed.", style="bold white")


def is_homebrew_installed():
    """Check if Homebrew is installed on macOS"""
    try:
        subprocess.run(['brew', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_homebrew():
    """Install Homebrew package manager for macOS"""
    console.print("Installing Homebrew...", style="bold yellow")
    try:
        install_cmd = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        subprocess.run(install_cmd, shell=True, check=True)
        console.print("✓ Homebrew installed successfully!", style="bold green")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"✗ Failed to install Homebrew: {e}", style="bold red")
        return False


def assist():
    banner_assist()


def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping, timeout=5)
        return True
    except:
        return False


def upgrade_pip():
    try:
        subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        updated_version = subprocess.check_output(['pip3', '--version']).decode().strip()
        console.print(f"✓ pip upgraded: {updated_version}", style="bold green")
    except subprocess.CalledProcessError as e:
        console.print(f"✗ Failed to upgrade pip: {e}", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


def install_package(package_name):
    try:
        subprocess.run(['python3', '-m', 'pip', 'install', package_name], check=True)
        console.print(f"✓ Successfully installed {package_name}", style="bold green")
    except subprocess.CalledProcessError as e:
        console.print(f"✗ Failed to install {package_name}: {e}", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


# macOS-specific package lists
basic_modules_macos = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 
    'docutils', 'pyyaml', 'python-dotenv', 'pillow', 'ipython', 'rich', 'click'
]

advanced_modules_macos = [
    'pytz', 'typing_extensions', 'jsonschema', 'pydantic', 'attrs', 'pydantic-core', 'orjson', 'ujson'
]

science_modules_macos = [
    'numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-image', 'statsmodels', 'sympy', 'networkx', 
    'biopython', 'h5py', 'numba', 'Cython', 'pandas-profiling', 'pytest', 'openpyxl', 'xlrd', 
    'scrapy', 'tabula-py', 'geopandas', 'pyproj', 'numexpr', 'pint', 'patsy', 'arviz'
]

computer_vision_modules_macos = [
    'opencv-python', 'opencv-contrib-python', 'Pillow', 'imageio', 'pytesseract', 'pyautogui', 
    'pyzbar', 'albumentations', 'scikit-image', 'mediapipe', 'face_recognition', 'imgaug', 
    'imagehash', 'scikit-video'
]

machine_learning_modules_macos = [
    'scikit-learn', 'tensorflow', 'keras', 'xgboost', 'lightgbm', 'catboost', 'shap',
    'pandas', 'dask', 'mlxtend', 'imbalanced-learn', 'optuna', 'hyperopt', 'mlflow', 'pymc3', 
    'h2o', 'ray', 'featuretools', 'category-encoders', 'scikit-optimize', 'prophet'
]

deep_learning_tensorflow_modules_macos = [
    'tensorflow', 'keras', 'tensorboard', 'keras-rl', 'keras-tuner',
    'tensorflow-addons', 'tensorflow-datasets', 'tensorflow-hub', 'tensorflow-probability',
    'tensorboard', 'tensorboardX', 'onnx', 'onnxruntime', 'tf2onnx'
]

deep_learning_pytorch_modules_macos = [
    'torch', 'torchvision', 'torchaudio', 'pytorch-lightning', 'torchmetrics',
    'transformers', 'fastai', 'accelerate', 'timm', 'einops',
    'onnx', 'onnxruntime', 'tensorboard', 'tensorboardX'
]

full_stack_development_modules_macos = [
    'flask', 'django', 'fastapi', 'sqlalchemy', 'pymongo', 'pytest', 
    'gunicorn', 'uvicorn', 'celery', 'redis', 'aiohttp', 'starlette', 'httpx',
    'jinja2', 'marshmallow', 'alembic', 'databases', 'tortoise-orm', 'pydantic',
    'loguru', 'structlog', 'sentry-sdk', 'watchdog', 'click', 'typer'
]

network_modules_macos = [
    'requests', 'httpx', 'aiohttp', 'websockets', 'flask', 'django',
    'paramiko', 'dnspython', 'pyftpdlib', 'twisted', 'pyngrok', 'netmiko', 'scapy'
]

build_modules_macos = [
    'pep517', 'setuptools', 'build', 'wheel', 'pytoml', 'cmake',
    'ninja', 'meson', 'cibuildwheel', 'twine', 'bump2version'
]

jupyter_modules_macos = [
    'jupyter', 'notebook', 'jupyterlab', 'nbconvert', 'nbformat', 'ipywidgets', 
    'ipykernel', 'voila', 'jupyter_contrib_nbextensions', 'jupyter_dash', 'jupytext', 
    'jupyterhub', 'jupyter_client', 'qtconsole', 'jupyterlab-widgets'
]

data_visualization_modules_macos = [
    'matplotlib', 'seaborn', 'plotly', 'bokeh', 'altair', 'holoviews', 'geopandas', 
    'folium', 'chart-studio', 'hvplot', 'pygal', 'missingno', 'pandas_profiling', 
    'pywaffle', 'yellowbrick', 'networkx', 'graphviz', 'dash', 'plotnine', 'kaleido'
]

database_modules_macos = [
    'sqlalchemy', 'pymysql', 'psycopg2-binary', 'pymongo', 'tinydb', 
    'redis', 'aioredis', 'aiomysql', 'pony', 'orm', 'dataset', 'datasets', 'peewee', 
    'asyncpg', 'duckdb', 'sqlmodel'
]

cybersecurity_modules_macos = [
    'cryptography', 'pycryptodome', 'paramiko', 'scapy', 'pyshark', 'dnspython', 'impacket', 
    'requests', 'flask-security', 'django-guardian', 'pyOpenSSL', 'certifi',
    'python-nmap', 'jinja2', 'pyjwt', 'passlib', 'bcrypt', 'keyring'
]

cloud_computing_modules_macos = [
    'boto3', 'botocore', 'google-cloud', 'google-cloud-storage', 'azure', 'azure-storage-blob', 
    'awscli', 'cloudpickle', 'apache-libcloud', 'kubernetes', 'docker', 'docker-compose',
    'cloudinary', 'paramiko', 'troposphere'
]

devops_modules_macos = [
    'ansible', 'fabric', 'invoke', 'pre-commit', 'pyinfra', 'gitpython', 
    'python-gitlab', 'pyyaml', 'jinja2', 'click', 'typer'
]

big_data_modules_macos = [
    'pyspark', 'dask', 'ray', 'modin', 'polars', 'pyarrow', 'fastparquet', 
    'h5py', 'tables', 'zarr', 'datashader', 'pandas', 'pandas-profiling', 'vaex'
]

nlp_modules_macos = [
    'spacy', 'nltk', 'gensim', 'transformers', 'textblob', 'sentence-transformers', 
    'fasttext', 'flair', 'tokenizers', 'sumy'
]

audio_modules_macos = [
    'librosa', 'soundfile', 'pydub', 'torchaudio', 'audioread', 'noisereduce', 
    'sounddevice', 'praat-parselmouth'
]

web_framework_modules_macos = [
    'fastapi', 'flask', 'django', 'starlette', 'uvicorn', 'gunicorn', 'httpx', 
    'requests', 'sqlmodel', 'fastapi-users', 'pydantic-settings'
]

geospatial_modules_macos = [
    'geopandas', 'shapely', 'fiona', 'rasterio', 'pyproj', 'rtree', 'geopy', 
    'contextily', 'osmnx'
]

testing_modules_macos = [
    'pytest', 'hypothesis', 'tox', 'coverage', 'pytest-xdist', 'pytest-cov', 
    'pytest-mock', 'pytest-asyncio', 'faker', 'factory-boy'
]

# macOS-specific tools (via Homebrew)
macos_dev_tools = {
    "Programming Languages": [
        "python3", "node", "go", "rust", "ruby", "java", "kotlin", "swift"
    ],
    "Development Tools": [
        "git", "vim", "neovim", "tmux", "wget", "curl", "htop", "tree", 
        "jq", "grep", "ripgrep", "fd", "bat", "exa", "fzf"
    ],
    "Database Tools": [
        "postgresql", "mysql", "redis", "mongodb-community", "sqlite"
    ],
    "Container & Orchestration": [
        "docker", "docker-compose", "kubernetes-cli", "helm", "minikube"
    ],
    "Security Tools": [
        "nmap", "wireshark", "openssl", "gnupg", "hashcat", "john-jumbo"
    ],
    "Network Tools": [
        "tcpdump", "netcat", "telnet", "mtr", "ngrep", "socat", "iperf3"
    ],
    "Version Control": [
        "git", "git-lfs", "gh", "gitlab-runner"
    ],
    "Cloud CLI": [
        "awscli", "azure-cli", "google-cloud-sdk"
    ],
    "Terminal Enhancements": [
        "zsh", "fish", "starship", "oh-my-zsh", "powerline-go"
    ]
}

module_types_macos = [
    None,
    'Basic Modules macOS',
    'Advanced Modules macOS',
    'Science Modules macOS',
    'Computer Vision Modules macOS',
    'Machine Learning Modules macOS',
    'Deep Learning TensorFlow Modules macOS',
    'Deep Learning PyTorch Modules macOS',
    'Full Stack Development Modules macOS',
    'Network Modules macOS',
    'Build Modules macOS',
    'Jupyter Modules macOS',
    'Data Visualization Modules macOS',
    'Database Modules macOS',
    'Cybersecurity Modules macOS',
    'Cloud Computing Modules macOS',
    'DevOps Modules macOS',
    'Big Data Modules macOS',
    'NLP Modules macOS',
    'Audio Modules macOS',
    'Web Framework Modules macOS',
    'Geospatial Modules macOS',
    'Testing Modules macOS',
    'macOS Development Tools (Homebrew)',
]


def install_brew_packages(packages):
    """Install a list of packages using Homebrew."""
    for package in packages:
        console.print(f"Installing {package}...", style="bold yellow")
        try:
            subprocess.run(["brew", "install", package], check=True)
            console.print(f"✓ {package} installed", style="bold green")
        except subprocess.CalledProcessError:
            console.print(f"✗ Failed to install {package}. Skipping.", style="bold red")


def display_brew_categories():
    """Display available Homebrew tool categories."""
    console.print("\nAvailable macOS Tool Categories (via Homebrew):", style="bold cyan")
    for idx, category in enumerate(macos_dev_tools.keys(), 1):
        console.print(f"{idx}. {category}", style="bold white")
    console.print("0. Back to main menu", style="bold white")


def macos_tools_run():
    """Install macOS development tools via Homebrew."""
    if not is_homebrew_installed():
        console.print("⚠️  Homebrew is not installed!", style="bold yellow")
        install_choice = Prompt.ask(
            "[bold green]Would you like to install Homebrew?[/]",
            choices=["y", "n"],
            default="y"
        )
        if install_choice.lower() == 'y':
            if not install_homebrew():
                console.print("Cannot proceed without Homebrew.", style="bold red")
                return
        else:
            console.print("Cannot install tools without Homebrew.", style="bold red")
            return
    
    while True:
        display_brew_categories()
        choice = Prompt.ask("\nEnter the number of the category", default="0")
        
        if choice == "0":
            console.print(f"Thank you for using PYMODINS, {user}! ❤️", style="bold green")
            break
        
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(macos_dev_tools):
                category = list(macos_dev_tools.keys())[choice_int - 1]
                tools = macos_dev_tools[category]
                console.print(f"\n[bold cyan]Selected Category:[/] {category}")
                console.print(f"[bold white]Tools to be installed:[/] {', '.join(tools)}")
                confirm = Prompt.ask("Do you want to proceed?", choices=["y", "n"], default="n")
                if confirm.lower() == 'y':
                    install_brew_packages(tools)
                    console.print("✓ Installation complete!", style="bold green")
                else:
                    console.print("Installation cancelled.", style="bold yellow")
            else:
                console.print("Invalid choice. Please try again.", style="bold red")
        except ValueError:
            console.print("Please enter a valid number.", style="bold red")


def clear():
    return subprocess.run(['clear'], check=True)


def install_rust():
    """Install Rust programming language on macOS"""
    try:
        console.print("Installing Rust via rustup...", style="bold yellow")
        subprocess.run(['curl', '--proto', '=https', '--tlsv1.2', '-sSf', 
                       'https://sh.rustup.rs', '-o', '/tmp/rustup.sh'], check=True)
        subprocess.run(['sh', '/tmp/rustup.sh', '-y'], check=True)
        console.print("✓ Rust installed successfully.", style="bold green")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"✗ Failed to install Rust: {e}", style="bold red")
        webbrowser.open('https://www.rust-lang.org/tools/install')
        return False


def log_mod(module_type, module_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Installed {module_name} from {module_type}"
    with open("module_installation_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")


def run():
    if not internet():
        banner_nointernet()
        return
    
    if sys.platform != 'darwin':
        banner()
        console.print("\t⚠️  This program is designed to run on macOS only.", style="bold yellow")
        return
    
    upgrade_pip()
    clear()
    banner()
    sys_info()
    
    install_type = Prompt.ask(
        "\n[bold green]What would you like to install?[/]\n"
        "  1. macOS Development Tools (via Homebrew)\n"
        "  2. Python Packages (via pip)\n"
        "Enter your choice",
        choices=["1", "2"],
        default="2"
    )
    
    if install_type == "1":
        try:
            macos_tools_run()
        except Exception as e:
            console.print(f"Error occurred: {e}", style="bold red")
    
    elif install_type == "2":
        module_types = [
            'Basic Modules macOS',
            'Advanced Modules macOS',
            'Science Modules macOS',
            'Computer Vision Modules macOS',
            'Machine Learning Modules macOS',
            'Deep Learning TensorFlow Modules macOS',
            'Deep Learning PyTorch Modules macOS',
            'Full Stack Development Modules macOS',
            'Network Modules macOS',
            'Build Modules macOS',
            'Jupyter Modules macOS',
            'Data Visualization Modules macOS',
            'Database Modules macOS',
            'Cybersecurity Modules macOS',
            'Cloud Computing Modules macOS',
            'DevOps Modules macOS',
            'Big Data Modules macOS',
            'NLP Modules macOS',
            'Audio Modules macOS',
            'Web Framework Modules macOS',
            'Geospatial Modules macOS',
            'Testing Modules macOS',
        ]
        
        console.print("\n[bold cyan]Select the type of Python modules to install:[/]\n")
        for i, module_type in enumerate(module_types, 1):
            console.print(f"{i}. {module_type}", style="bold white")
        
        try:
            selected_module_type = int(Prompt.ask("\nEnter the number corresponding to your choice"))
            if 1 <= selected_module_type <= len(module_types):
                clear()
                selected_module_type = module_types[selected_module_type - 1]
                console.print(f"\n[bold green]Selected Module Type:[/] {selected_module_type}")
                console.print("\n[bold cyan]Modules:[/]")
                modules = globals().get(selected_module_type.lower().replace(" ", "_"), [])
                
                for i, module in enumerate(modules, 1):
                    console.print(f"{i}. {module}", style="bold white")
                
                install_option = Prompt.ask(
                    "\nDo you want to install all modules in this section?",
                    choices=["yes", "y", "no", "n"],
                    default="no"
                )
                clear()
                
                if install_option.lower() in ["yes", "y"]:
                    for module in modules:
                        if module == 'rust':
                            console.print("⚠️  Module rust needs to be installed separately.", style="bold yellow")
                            rust_choice = Prompt.ask("Do you want to install Rust?", choices=["y", "n"], default="n")
                            if rust_choice.lower() == "y":
                                if not install_rust():
                                    continue
                        
                        clear()
                        
                        try:
                            subprocess.run(['pip3', 'install', module], check=True)
                            log_mod(selected_module_type, module)
                            console.print(f"✓ {module} installed successfully.", style="bold green")
                        except subprocess.CalledProcessError as e:
                            console.print(f"✗ Failed to install {module}: {e}", style="bold red")
                    
                    console.print("\n✓ All modules installed successfully!", style="bold green")
                    more = Prompt.ask("Do you want to install more?", choices=["yes", "y", "no", "n"], default="no")
                    if more.lower() in ["no", "n"]:
                        console.print(f"Thank you for using PYMODINS, {user}! ❤️", style="bold green")
                        sys.exit()
                    elif more.lower() in ["yes", "y"]:
                        run()
                else:
                    console.print("\n[bold cyan]Modules:[/]")
                    modules = globals().get(selected_module_type.lower().replace(" ", "_"), [])
                    for i, module in enumerate(modules, 1):
                        console.print(f"{i}. {module}", style="bold white")
                    
                    module_index = int(Prompt.ask("Enter the number corresponding to the module to install (type '0' to exit)"))
                    
                    if module_index == 0:
                        console.print("\nReload this program to install new modules.", style="bold yellow")
                        sys.exit()
                    
                    selected_module = modules[module_index - 1]
                    
                    if selected_module == 'rust':
                        if not install_rust():
                            sys.exit()
                    
                    try:
                        subprocess.run(['pip3', 'install', selected_module], check=True)
                        log_mod(selected_module_type, selected_module)
                        console.print(f"✓ {selected_module} installed successfully.", style="bold green")
                    except subprocess.CalledProcessError as e:
                        console.print(f"✗ Failed to install {selected_module}: {e}", style="bold red")
                    
                    more = Prompt.ask("Do you want to install more?", choices=["yes", "y", "no", "n"], default="no")
                    if more.lower() in ["no", "n"]:
                        console.print(f"Thank you for using PYMODINS, {user}! ❤️", style="bold green")
                        sys.exit()
                    elif more.lower() in ["yes", "y"]:
                        run()
            
            else:
                console.print("Invalid selection. Please enter a valid number.", style="bold red")
        
        except Exception as e:
            console.print(f"Error: {e}\nPlease try again.", style="bold red")
            run()
