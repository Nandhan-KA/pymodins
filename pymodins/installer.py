import os
import getpass
import sys
import pip
import urllib.request
from datetime import datetime
import subprocess
import ctypes
import webbrowser
from rich.console import Console


user = getpass.getuser()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def run_as_admin():
    if not is_admin():
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]]) 
        print(f"Re-running {script} with admin privileges.")
        try:
            subprocess.check_call(["powershell.exe", "-Command", f"Start-Process 'python' -ArgumentList '\"{script}\" {params}' -Verb RunAs"])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running as admin: {e}")
            return False
    else:
        print("Already running with admin privileges.")
        return True


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
    ascii_art="""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v2.2.0               
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\t For more info contact: developer.nandhank@gmail.com", style="bold green")

def banner_assist():
    console = Console()
    ascii_art="""              
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
    console.print("Pymodins Virtual Assistant")

def banner_nointernet():
    console = Console()
    ascii_art="""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v2.2.0                
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\t For more info contact: developer.nandhank@gmail.com", style="bold green")
    console.print(" \n \t This Project Requires Internet Connection 🌐 ", style="bold yellow")

def creator():
    console = Console()
    ascii_art="""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                v2.2.0                
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\t For more info contact: developer.nandhank@gmail.com", style="bold green")

def sys_info():
    console = Console()
    console.print("System Platform:", sys.platform, style="bold white")
    console.print("Python version:", sys.version,style="bold white")
    try:
        pip_version = subprocess.check_output(['pip', '--version']).decode().strip()
        console.print("pip version:", pip_version,style="bold white")
        if is_admin():
            console.print("Admin Previledges: True",style="bold white")
        else:
            console.print("Admin Previledges: False",style="bold white")
    except Exception as e:
        console.print("Error:", e, "Reinstall Python with PIP and add PIP to the System PATH",style="bold white")
        
        
def assist():
    banner_assist()

def upgrade_pip():
    try:
        subprocess.run(['python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        print(f"pip upgraded to version {pip.__version__}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")
    except Exception as e:
        print(f"Error: {e}")
        
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
                    'powershell.exe '
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

basic_modules = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 'docutils', 'pyyaml', 'python-dotenv', 'pillow',
      'datetime',  'statistics',  'configparser'
]

advanced_modules = [
    'argparse', 'asyncio', 'dataclasses', 'pytz', 'pathlib', 'typing_extensions', 'jsonschema', 'pydantic'
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
    'pyproject.toml', 'ninja', 'meson', 'scons', 'bazel', 'autoconf', 'automake', 'libtool', 'rust'
]

jupyter_modules = [
    'jupyter',
    'notebook', 'jupyterlab', 'nbconvert', 'nbformat', 'ipywidgets', 'ipykernel', 'voila', 'jupyter_contrib_nbextensions', 'jupyter_dash', 'jupyter_bokeh', 'jupytext', 'jupyterhub', 'jupyter_client', 'qtconsole'
]

data_visualization_modules = [
    'matplotlib', 'seaborn', 'plotly', 'bokeh', 'altair', 'holoviews', 'geopandas', 'folium', 'chart-studio', 'pyecharts',
    'hvplot', 'pygal', 'missingno', 'pandas_profiling', 'pywaffle', 'yellowbrick', 'networkx', 'graphviz', 'dash', 
    'tableau', 'vispy', 'toyplot'
]

database_modules = [
    'sqlalchemy', 'pymysql', 'psycopg2', 'sqlite3', 'mongodb', 'pymongo', 'tinydb', 'couchdb', 'cassandra-driver', 'happybase',
    'redis', 'aioredis', 'aiomysql', 'pony', 'orm', 'orator', 'dataset', 'datasets', 'peewee', 'sqlalchemy-migrate', 'yoyo-migrations'
]

cybersecurity_modules = [
    'cryptography', 'pycryptodome', 'paramiko', 'scapy', 'pyshark', 'dnspython', 'impacket', 'requests', 'flask-security', 
    'django-guardian', 'mitmproxy', 'pyOpenSSL', 'certifi', 'ssl', 'keyring', 'hpack', 'brotli', 'hashlib', 'python-nmap', 
    'jinja2', 'pyjwt', 'passlib'
]

cloud_computing_modules = [
    'boto3', 'google-cloud', 'azure', 'awscli', 'cloudpickle', 'cloudmesh', 'apache-libcloud', 'terraform', 'pulumi', 'ansible',
    'kubernetes', 'docker', 'docker-compose', 'pywren', 'serverless', 'salt', 'pyinfra', 'cloudinary', 'paramiko', 'cloudant', 
    'python-openstackclient', 'troposphere'
]

devops_modules = [
    'ansible', 'jenkins', 'travis-ci', 'git', 'docker', 'docker-compose', 'kubernetes', 'vagrant', 'puppet', 'chef', 
    'salt', 'fabric', 'terraform', 'consul', 'nomad', 'packer', 'helm', 'spinnaker', 'circleci', 'bamboo', 'gitlab', 
    'gitea', 'hugo', 'mkdocs', 'pre-commit', 'pyinfra'
]

big_data_modules = [
    'pyspark', 'hadoop', 'kafka', 'dask', 'ray', 'modin', 'polars', 'koalas', 'pyarrow', 'fastparquet', 
    'pydoop', 'pyhive', 'mrjob', 'h5py', 'tables', 'zarr',  'petastorm', 'cudf', 'datashader', 'blaze', 
    'turicreate', 'pandas', 'pandas-profiling'
]


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
    'Jupyter Modules',
    'Data Visualization Modules',
    'Database Modules',
    'Cybersecurity Modules',
    'Cloud Computing Modules',
    'DevOps Modules',
    'Big Data Modules',
]

def installer():
    if internet() and sys.platform == 'win32':
        upgrade_pip()
        clear()
        banner()
        sys_info()
        module_types = [
    'Basic Modules',
    'Advanced Modules',
    'Science Modules',
    'Computer Vision Modules',
    'Machine Learning Modules',
    'Deep Learning Modules',
    'Full Stack Development Modules',
    'Network Modules',
    'Build Modules',
    'Jupyter Modules',
    'Data Visualization Modules',
    'Database Modules',
    'Cybersecurity Modules',
    'Cloud Computing Modules',
    'DevOps Modules',
    'Big Data Modules',
]

        print("\nPlease select the type of modules you want to install:\n")
        for i, module_type in enumerate(module_types, 1):
            print(f"{i}. {module_type}")

        try:
            selected_module_type = int(
                input("\nEnter the number corresponding to your choice: "))

            if 1 <= selected_module_type <= len(module_types):
                clear()
                selected_module_type = module_types[selected_module_type - 1]
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
                            result = ctypes.windll.user32.MessageBoxW(0, "Do you want to continue?", "Alert", 0x40 | 0x1)
                            if result==1:
                                print("Module dlib has to be installed after you have installed visual studio build tools")
                                x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                                if x == "y":
                                    if install_vscode_build_tools():
                                        print("Build tools installed successfully.")
                                    else:
                                        print("Failed to install build tools.")
                                        continue
                            else:
                                pass  
                        
                        if module == 'rust':
                            result = ctypes.windll.user32.MessageBoxW(0, "This Modules Required VSBuild tools.\n Do you want to continue?", "Alert", 0x40 | 0x1)
                            if result==1:
                                print("Module rust needs to be installed separately.")
                                x = input("Do you want to install Rust? (y/n): ").lower()
                                if x == "y":
                                    if install_rust():
                                        print("Rust installed successfully.")
                                    else:
                                        print("Failed to install Rust. Opening the Rust installation webpage.")
                                        webbrowser.open('https://www.rust-lang.org/tools/install')
                                        break  
                            else:
                                pass

                        clear()
                        
                        try:
                            command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                            os.system(command)
                            log_mod(selected_module_type, module, python_folder)
                        except:
                            command = f"cd C:\\Program Files\\python\\{python_folder}\\Scripts && pip.exe install {module}"
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
                    print("Modules:")
                    modules = globals()[
                        selected_module_type.lower().replace(" ", "_")]
                    for i, module in enumerate(modules, 1):
                        print(f"{i}. {module}")

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
                    
                    if selected_module == 'dlib':
                        print("Module dlib has to be installed after you have installed visual studio build tools")
                        x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                        if x == "y":
                            if install_vscode_build_tools():
                                print("Build tools installed successfully.")
                            else:
                                print("Failed to install build tools.")
                                sys.exit()  
                    
                    if selected_module == 'rust':
                        print("Module rust needs to be installed separately.")
                        x = input("Do you want to install Rust? (y/n): ").lower()
                        if x == "y":
                            if install_rust():
                                print("Rust installed successfully.")
                            else:
                                print("Failed to install Rust. Opening the Rust installation webpage.")
                                webbrowser.open('https://www.rust-lang.org/tools/install')
                                sys.exit()  

                    try:
                        path1 = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {module}"
                        os.system(path1)
                        log_mod(selected_module_type, module, python_folder)
                    except:
                        path2 = f"cd C:\\Program Files\\python\\{python_folder}\\Scripts && pip.exe install {module}"
                        os.system(path2)
                        log_mod(selected_module_type, module, python_folder)

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
            
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    
    else:
        banner_nointernet()

def install_basic_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 1

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_basic_modules()
    else:
        banner_nointernet()

def install_advanced_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 2
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
                    
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_advanced_modules()
        
    else:
        banner_nointernet()


def install_machinelearning_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 5
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_machinelearning_modules()
    else:
        banner_nointernet()


def install_deeplearning_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 6
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_deeplearning_modules()
    else:
        banner_nointernet()


def install_fullstack_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 7
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_fullstack_modules()
    else:
        banner_nointernet()


def install_science_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 3
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_science_modules()
    else:
        banner_nointernet()

      
def install_computervision_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 4
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
                    
                if selected_module == 'dlib':
                     
                    print("Module dlib has to be installed after you have installed visual studio build tools")
                    x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                    if x == "y":
                        if install_vscode_build_tools():
                            print("Build tools installed successfully.")
                        else:
                            print("Failed to install build tools.")
                                
                    
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
                os.system(command)

                more = input("Do you want to install more? (Yes/No): ")
                if more.lower() in ["no", "n"]:
                    print(f"{user} Thank you for using.")
                    sys.exit()
                elif more.lower() in ["yes", "y"]:
                    installer()
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_computervision_modules()
    else:
        banner_nointernet()

       
def install_network_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 8
        

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_network_modules()
    else:
        banner_nointernet()


def install_build_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 9
        

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
                         
                        print("Installing VSBuild Tools")
                        install_vscode_build_tools()
                        clear
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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
                    
                if selected_module == 'rust':
                     
                    print("Installing VSBuild Tools")
                    install_vscode_build_tools()
                    clear
                     
                    print("Module rust needs to be installed separately.")
                    x = input("Do you want to install Rust? (y/n): ").lower()
                    if x == "y":
                        if install_rust():
                            print("Rust installed successfully.")
                        else:
                            print("Failed to install Rust. Opening the Rust installation webpage.")
                            webbrowser.open('https://www.rust-lang.org/tools/install')
                            
                command = f"cd C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{python_folder}\\Scripts && pip.exe install {selected_module}"
                os.system(command)

                more = input("Do you want to install more? (Yes/No): ")
                if more.lower() in ["no", "n"]:
                    print(f"{user} Thank you for using.")
                    sys.exit()
                elif more.lower() in ["yes", "y"]:
                    installer()
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_build_modules()
    else:
        banner_nointernet()

def install_jupyter_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 10
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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")
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
            
    elif internet() and sys.platform == "linux":
        banner()
        Console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
        return
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_jupyter_modules()
    else:
        banner_nointernet()

def install_data_visualization_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 11

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_data_visualization_modules()    
    else:
        banner_nointernet()


def install_database_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 12

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_database_modules()   
    else:
        banner_nointernet()



def install_CyberSecurity_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 13

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_CyberSecurity_modules()    
    else:
        banner_nointernet()


def install_cloudcomputing_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 14

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_cloudcomputing_modules()    
    else:
        banner_nointernet()


def install_devops_modules():
    if internet() and sys.platform == 'win32' and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 15

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_devops_modules()     
    else:
        banner_nointernet()


def install_bigdata_modules():
    if internet() and sys.platform == 'win32'and is_admin():
        upgrade_pip()
        banner()
        sys_info()
        selected_option = 16

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
                print("Modules:")
                modules = globals()[
                selected_module_type.lower().replace(" ", "_")]
                for i, module in enumerate(modules, 1):
                    print(f"{i}. {module}")

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
                    
    elif internet() and sys.platform == "linux":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Windows systems only.", style="bold yellow")
    elif internet() and sys.platform == 'win32' and not is_admin():
        run_as_admin()
        install_bigdata_modules()     
    else:
        banner_nointernet()
          
def run():
    if is_admin():
        installer()  
    else:
        if run_as_admin():
            pass  
        else:
            raise PermissionError("Failed to acquire administrative privileges.")
 
