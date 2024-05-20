import os
import getpass
import sys
import ctypes
import subprocess
import webbrowser
import pymsgbox
import urllib.request
from datetime import datetime
from rich.console import Console

user = getpass.getuser()
version="0.1.8"
def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping)
        return True
    except:
        return False


def os_platform():
    platform = {
        'win32': 'Windows'
    }
    if sys.platform not in platform:
        return sys.platform
    return platform[sys.platform]


def banner():
    console = Console()

    ascii_art = """
              \ |   \    \ | _ \ |  |   \    \ |    |  / 
             .  |  _ \  .  | |  |__ |  _ \  .  |    . <  
            _|\_|_/  _\_|\_|___/_| _|_/  _\_|\_|   _|\_\ 
            """
    console.print(ascii_art, style="bold yellow")
    console.print("Creator: Nandhan K", style="bold cyan")
    console.print("Github: @github.com/Nandhan-KA", style="bold yellow")


def sys_info():
    print("System Platform:", sys.platform)
    print("Python verion:", sys.version)
    print("pymodins Version:",version )


def clear():
    return os.system('cls')


def log_mod(module_type, module_name, python_folder):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Installed {module_name} from {module_type} in {python_folder}"
    with open("module_installation_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

def install_vscode_build_tools():
    def run_command(command):
        result = subprocess.run(command, shell=True)
        return result.returncode

    def install_chocolatey():
        choco_install_cmd = (
            '@"%"SystemRoot%"\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" '
            '-NoProfile -InputFormat None -ExecutionPolicy Bypass -Command '
            '"iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" '
            '&& SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"'
        )
        return run_command(choco_install_cmd)

    def install_vs_build_tools():
        vs_build_tools_cmd = 'choco install -y visualstudio2019buildtools'
        return run_command(vs_build_tools_cmd)

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("This script requires administrator privileges. Please run as an administrator.")
        return False

    choco_installed = subprocess.run("choco -v", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if choco_installed.returncode != 0:
        if install_chocolatey() != 0:
            print("Failed to install Chocolatey.")
            return False

    if install_vs_build_tools() != 0:
        print("Failed to install Visual Studio Build Tools.")
        return False

    print("Installation of Visual Studio Build Tools completed successfully.")
    return True

def install_rust():
    def run_command(command):
        result = subprocess.run(command, shell=True)
        return result.returncode

    def download_rust_installer():
        url = "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
        installer_path = os.path.join(os.getenv('TEMP'), 'rustup-init.exe')
        try:
            urllib.request.urlretrieve(url, installer_path)
            return installer_path
        except Exception as e:
            print(f"Failed to download Rust installer: {e}")
            return None

    def install_rustup(installer_path):
        rustup_install_cmd = f'"{installer_path}" -y'
        return run_command(rustup_install_cmd)

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("This script requires administrator privileges. Please run as an administrator.")
        return False

    installer_path = download_rust_installer()
    if not installer_path:
        print("Failed to download Rust installer. Opening the Rust installation webpage.")
        webbrowser.open('https://www.rust-lang.org/tools/install')
        return False

    if install_rustup(installer_path) != 0:
        print("Failed to install Rust. Opening the Rust installation webpage.")
        webbrowser.open('https://www.rust-lang.org/tools/install')
        return False

    print("Installation of Rust completed successfully.")
    return True


# Module Lists
basic_modules = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 'docutils', 'pyyaml', 'python-dotenv', 'pillow',
]

advanced_modules = [
    'argparse', 'asyncio', 'collections', 'contextlib', 'dataclasses', 'pytz', 'pathlib', 'typing_extensions',
        'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 'docutils', 'pyyaml', 'python-dotenv', 'pillow',

]

science_modules = [
    'numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-image', 'statsmodels', 'sympy', 'networkx', 'biopython',
    'h5py', 'numba', 'Cython', 'pandas-profiling', 'pytest', 'openpyxl', 'xlrd', 'scrapy', 'tabula-py', 'geopandas', 'pyproj'
]

computer_vision_modules = [
    'opencv-python', 'Pillow', 'imageio', 'pytesseract', 'pyautogui', 'pyzbar', 'dlib',
    'albumentations', 'scikit-image', 'mediapipe', 'mmcv', 'mmdet', 'face_recognition', 'imgaug', 'simplecv'
]

machine_learning_modules = [
    'scikit-learn', 'tensorflow', 'keras', 'xgboost', 'lightgbm', 'catboost', 'shap',
    'pandas', 'dask', 'mlxtend', 'imbalanced-learn', 'optuna', 'hyperopt', 'mlflow', 'pymc3', 'h2o', 'ray'
]

deep_learning_modules = [
    'torch', 'pytorch-lightning', 'transformers', 'fastai', 'keras-rl', 'tensorboard',
    'onnx', 'onnxruntime', 'mxnet', 'chainer', 'deeplearning4j', 'paddlepaddle', 'theano', 'lasagne', 'gluonts'
]

full_stack_development_modules = [
    'flask', 'django', 'fastapi', 'express', 'sqlalchemy', 'django-orm', 'mongodb', 'mongoose', 'react', 'vue', 'angular', 'jquery', 'bootstrap', 'tailwindcss', 'swagger', 'postman', 'git', 'github-cli', 'docker', 'docker-compose', 'kubernetes', 'nginx', 'apache', 'oauthlib', 'python-social-auth', 'passport', 'pytest', 'jest', 'ansible', 'jenkins', 'travis-ci', 'prometheus', 'grafana', 'elk-stack', 'redis', 'celery', 'graphql', 'socket.io',
    'tornado', 'bottle', 'cherrypy', 'pyramid', 'pylons', 'web2py', 'WTForms', 'jinja2', 'marshmallow', 'connexion', 'drf-yasg', 'fastapi', 'gunicorn', 'uWSGI', 'hypercorn', 'supervisor', 'celery', 'kombu', 'flower', 'alembic', 'asyncpg', 'databases', 'twisted', 'starlette', 'aiohttp', 'gevent', 'eventlet', 'tqdm', 'progressbar2', 'Faker', 'pyfakefs', 'factory_boy', 'schematics', 'tortoise-orm', 'ormar', 'pydantic', 'loguru', 'structlog', 'sentry-sdk', 'watchdog'
]

network_modules = [
    'socket', 'http.client', 'urllib', 'requests', 'socketIO-client', 'websockets', 'http.server', 'flask', 'django',
    'ftplib', 'smtplib', 'imaplib', 'poplib', 'telnetlib', 'paramiko', 'dnspython', 'pyftpdlib', 'twisted', 'pyngrok', 'snmp', 'netmiko', 'nmap', 'scapy'
]

build_modules = [
    'pep517', 'setuptools', 'build', 'wheel', 'pytoml', 'cmake',
    'pyproject.toml', 'ninja', 'meson', 'scons', 'bazel', 'autoconf', 'automake', 'libtool','rust'
]

jupyter_modules = [
    'jupyter',
    'notebook', 'jupyterlab', 'nbconvert', 'nbformat', 'ipywidgets', 'ipykernel', 'voila', 'jupyter_contrib_nbextensions', 'jupyter_dash', 'jupyter_bokeh', 'jupytext', 'jupyterhub', 'jupyter_client', 'qtconsole'
]


def installer():
    if internet():
        clear()
        try:
            if os_platform() == "Windows":
                pass
            else:
                print("This software is only for Windows. Exiting.")
                sys.exit()
            banner()

            print("""
            1. Basic Modules
            2. Advanced Modules
            3. Science Modules
            4. Computer Vision Modules
            5. Machine Learning Modules
            6. Deep Learning Modules
            7. Full Stack Development Modules
            8. Network Modules
            9. Build Modules
            10.Jupyter Modules
            """)

            selected_option = int(
                input("Enter the number corresponding to the module type: "))
            clear()
            module_types = [
                None,
                'Basic Modules',
                'Advanced Modules',
                'Science Modules',
                'Computer Vision Modules',
                'Machine Learning Modules',
                'Deep Learning Modules',
                'Full Stack Development Modules',
                'Network Modules',
                'Build Modules',
                'Jupyter Modules'
            ]

            selected_module_type = module_types[selected_option]

            if selected_module_type:
                print(f"\nSelected Module Type: {selected_module_type}")
                print("Modules:")
                modules = globals()[
                    selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

                install_option = input(
                    "Do you want to install all modules in this section? (Yes/No): ").lower()
                clear()
                if install_option in ["yes", "y"]:

                    versions = os.listdir(
                        f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

                    if len(versions) == 2:
                        print(f"\nYou have two folders in your Python installation:")
                        print("(1)", versions[0])
                        print("(2)", versions[1])
                        python_folder = versions[int(
                            input("Select your Python folder (1 or 2): ")) - 1]
                    else:
                        python_folder = str(*versions)

                    for module in modules:
                        if module == 'dlib':
                            pymsgbox.alert("This Modules Required VSBuild Tools")
                            print("Module dlib has to be installed after you have installed visual studio build tools")
                            x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                            if x == "y":
                                if install_vscode_build_tools():
                                    print("Build tools installed successfully.")
                                else:
                                    print("Failed to install build tools.")
                                    continue  
                        
                        if module == 'rust':
                            pymsgbox.alert("This Modules Required VSBuild Tools")
                            print("Module rust needs to be installed separately.")
                            x = input("Do you want to install Rust? (y/n): ").lower()
                            if x == "y":
                                if install_rust():
                                    print("Rust installed successfully.")
                                else:
                                    print("Failed to install Rust. Opening the Rust installation webpage.")
                                    webbrowser.open('https://www.rust-lang.org/tools/install')
                                    break
                        clear()
                        command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                        os.system(command)
                        log_mod(selected_module_type, module, python_folder)

                    print("\nAll modules installed successfully.")
                    more = input("Do you want to install more? (Yes/No): ")
                    if more.lower() in ["no", "n"]:
                        print(f"{user} Thank you for using.")
                        sys.exit()
                    elif more.lower() in ["yes", "y"]:
                        installer()
                else:
                    module_index = int(input(
                        "Enter the number corresponding to the module to install (type '0' to exit): "))

                    if module_index == 0:
                        print(
                            "\nReload this program to install new modules of Python.")
                        sys.exit()

                    selected_module = modules[module_index - 1]

                    versions = os.listdir(
                        f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

                    if len(versions) == 2:
                        print(f"\nYou have two folders in your Python installation:")
                        print("(1)", versions[0])
                        print("(2)", versions[1])
                        python_folder = versions[int(
                            input("Select your Python folder (1 or 2): ")) - 1]
                    else:
                        python_folder = str(*versions)
                    command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
                    os.system(command)

                    more = input("Do you want to install more? (Yes/No): ")
                    if more.lower() in ["no", "n"]:
                        print(f"{user} Thank you for using.")
                        sys.exit()
                    elif more.lower() in ["yes", "y"]:
                        installer()

            else:
                print("Invalid selection. Please enter a valid number.")

        except Exception as e:
            print("Error:", e, "\nPlease try again.")
            installer()
    else:
        print("No Internet Connection")



def run():
    installer()
    
def install_basic_modules():
    selected_option = 1
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_advanced_modules():
    selected_option = 2
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_machinelearning_modules():
    selected_option = 5
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_deeplearning_modules():
    selected_option = 6
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_fullstack_modules():
    selected_option = 7
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_science_modules():
    selected_option = 3
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()

def install_computervision_modules():
    selected_option = 4
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                if module == 'dlib':
                    pymsgbox.alert("This Modules Required VSBuild Tools")
                    print("Module dlib has to be installed after you have installed visual studio build tools")
                    x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                    if x == "y":
                        if install_vscode_build_tools():
                            print("Build tools installed successfully.")
                        else:
                            print("Failed to install build tools.")
                            continue  
                        
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()

def install_network_modules():
    selected_option = 8
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_build_modules():
    selected_option = 9
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                if module == 'rust':
                    pymsgbox.alert("This Modules Required VSBuild Tools")
                    print("Module rust needs to be installed separately.")
                    x = input("Do you want to install Rust? (y/n): ").lower()
                    if x == "y":
                        if install_rust():
                            print("Rust installed successfully.")
                        else:
                            print("Failed to install Rust. Opening the Rust installation webpage.")
                            webbrowser.open('https://www.rust-lang.org/tools/install')
                            break  

                    
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()


def install_jupyter_modules():
    selected_option = 10
    clear()
    module_types = [
        None,
        'Basic Modules',
        'Advanced Modules',
        'Science Modules',
        'Computer Vision Modules',
        'Machine Learning Modules',
        'Deep Learning Modules',
        'Full Stack Development Modules',
        'Network Modules',
        'Build Modules',
        'Jupyter Modules'
    ]

    selected_module_type = module_types[selected_option]

    if selected_module_type:
        print(f"\nSelected Module Type: {selected_module_type}")
        print("Modules:")
        modules = globals()[
            selected_module_type.lower().replace(" ", "_")]
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")

        install_option = input(
            "Do you want to install all modules in this section? (Yes/No): ").lower()
        clear()
        if install_option in ["yes", "y"]:

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)

            for module in modules:
                clear()
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                os.system(command)
                log_mod(selected_module_type, module, python_folder)

            print("\nAll modules installed successfully.")
            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
        else:
            module_index = int(input(
                "Enter the number corresponding to the module to install (type '0' to exit): "))

            if module_index == 0:
                print(
                    "\nReload this program to install new modules of Python.")
                sys.exit()

            selected_module = modules[module_index - 1]

            versions = os.listdir(
                f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Python")

            if len(versions) == 2:
                print(f"\nYou have two folders in your Python installation:")
                print("(1)", versions[0])
                print("(2)", versions[1])
                python_folder = versions[int(
                    input("Select your Python folder (1 or 2): ")) - 1]
            else:
                python_folder = str(*versions)
            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
            os.system(command)

            more = input("Do you want to install more? (Yes/No): ")
            if more.lower() in ["no", "n"]:
                print(f"{user} Thank you for using.")
                sys.exit()
            elif more.lower() in ["yes", "y"]:
                installer()
