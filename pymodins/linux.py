import os
import getpass
import sys
import pip
import time
import urllib.request
from datetime import datetime
import subprocess
import ctypes
import webbrowser
from rich.console import Console
from rich.prompt import Prompt

console=Console()
user=subprocess.run('whoami',check=True)

def banner():
    console = Console()
    ascii_art=r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v2.1.7               
    """
    console.print(ascii_art, style="bold yellow")
    console.print("Creator: Nandhan K", style="bold cyan")
    console.print("Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print("\n For more info contact: developer.nandhank@gmail.com", style="bold green")


def banner_assist():
    console = Console()
    ascii_art=r"""              
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
    ascii_art=r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                 v2.1.7                
    """
    console.print(ascii_art, style="bold yellow")
    console.print("\t Creator: Nandhan K", style="bold cyan")
    console.print("\t Github: @github.com/Nandhan-KA", style="bold yellow")
    console.print(" \n \t This Project Requires Internet Connection 🌐 ", style="bold yellow")
    console.print("\n For more info contact: developer.nandhank@gmail.com", style="bold green")

def creator():
    console = Console()
    ascii_art=r"""              
 _______  ____  ____  ____    ____   ___   ______   _____  ____  _____   ______   
|_   __ \|_  _||_  _||_   \  /   _|.'   `.|_   _ `.|_   _||_   \|_   _|.' ____ \  
  | |__) | \ \  / /    |   \/   | /  .-.  \ | | `. \ | |    |   \ | |  | (___ \_| 
  |  ___/   \ \/ /     | |\  /| | | |   | | | |  | | | |    | |\ \| |   _.____`.  
 _| |_      _|  |_    _| |_\/_| |_\  `-'  /_| |_.' /_| |_  _| |_\   |_ | \____) | 
|_____|    |______|  |_____||_____|`.___.'|______.'|_____||_____|\____| \______.' 
                                                                v2.1.7                
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
        pip_version = subprocess.check_output(['pip', '--version']).decode().strip()
        console.print(f"pip version: {pip_version}", style="bold white")
        if is_admin():
            console.print("Admin Privileges: True", style="bold white")
        else:
            console.print("Admin Privileges: False", style="bold white")
    except Exception as e:
        console.print(f"Error: {e}. Reinstall Python with PIP and ensure PIP is in the system PATH.", style="bold white")


def is_admin():
    return os.geteuid() == 0


def assist():
    banner_assist()


def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping)
        return True
    except:
        return False


def upgrade_pip():
    try:
        subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        updated_version = subprocess.check_output(['pip', '--version']).decode().strip()
        print(f"pip upgraded to version: {updated_version}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")
    except Exception as e:
        print(f"Error: {e}")


def install_package(package_name):
    try:
        subprocess.run(['python3', '-m', 'pip', 'install', package_name], check=True)
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")
    except Exception as e:
        print(f"Error: {e}")

        
basic_modules_linux = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 
    'docutils', 'pyyaml', 'python-dotenv', 'pillow'
]

advanced_modules_linux = [
    'pytz', 'typing_extensions', 'jsonschema', 'pydantic'
]

science_modules_linux = [
    'numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-image', 'statsmodels', 'sympy', 'networkx', 
    'biopython', 'h5py', 'numba', 'Cython', 'pandas-profiling', 'pytest', 'openpyxl', 'xlrd', 
    'scrapy', 'tabula-py', 'geopandas', 'pyproj'
]

computer_vision_modules_linux = [
    'opencv-python', 'Pillow', 'imageio', 'pytesseract', 'pyautogui', 'pyzbar', 'dlib', 
    'albumentations', 'scikit-image', 'mediapipe', 'mmcv', 'mmdet', 'face_recognition', 'imgaug', 'simplecv'
]

machine_learning_modules_linux = [
    'scikit-learn', 'tensorflow', 'keras', 'xgboost', 'lightgbm', 'catboost', 'shap', 
    'pandas', 'dask', 'mlxtend', 'imbalanced-learn', 'optuna', 'hyperopt', 'mlflow', 'pymc3', 'h2o', 'ray'
]

deep_learning_modules_linux = [
    'torch', 'pytorch-lightning', 'transformers', 'fastai', 'keras-rl', 'tensorboard', 
    'onnx', 'onnxruntime', 'mxnet', 'chainer', 'paddlepaddle', 'theano', 'lasagne', 'gluonts'
]

full_stack_development_modules_linux = [
    'flask', 'django', 'fastapi', 'sqlalchemy', 'django-orm', 'mongodb', 'mongoose', 
    'react', 'vue', 'angular', 'jquery', 'bootstrap', 'tailwindcss', 'swagger', 'postman', 
    'git', 'docker', 'docker-compose', 'kubernetes', 'nginx', 'apache', 'oauthlib', 'pytest', 'ansible', 
    'jenkins', 'prometheus', 'grafana', 'redis', 'celery', 'graphql', 'socket.io', 'tornado', 'gunicorn', 
    'uWSGI', 'supervisor', 'asyncpg', 'databases', 'starlette', 'aiohttp', 'tqdm', 'loguru', 'sentry-sdk', 'watchdog'
]

network_modules_linux = [
    'requests', 'socketIO-client', 'websockets', 
    'flask', 'django', 'paramiko', 
    'dnspython', 'pyftpdlib', 'twisted', 'pyngrok', 'scapy', 'netmiko', 'nmap', 'snmp'
]

build_modules_linux = [
    'pep517', 'setuptools', 'build', 'wheel', 'cmake', 'pyproject.toml', 'ninja', 
    'meson', 'scons', 'bazel', 'autoconf', 'automake', 'libtool', 'rust'
]

jupyter_modules_linux = [
    'jupyter', 'notebook', 'jupyterlab', 'nbconvert', 'nbformat', 'ipywidgets', 
    'ipykernel', 'voila', 'jupyter_contrib_nbextensions', 'jupyter_dash', 'jupyter_bokeh', 'jupytext', 
    'jupyterhub', 'jupyter_client', 'qtconsole'
]

data_visualization_modules_linux = [
    'matplotlib', 'seaborn', 'plotly', 'bokeh', 'altair', 'holoviews', 'geopandas', 
    'folium', 'chart-studio', 'pyecharts', 'hvplot', 'pygal', 'missingno', 'pandas_profiling', 
    'pywaffle', 'yellowbrick', 'networkx', 'graphviz', 'dash', 'vispy', 'toyplot'
]

database_modules_linux = [
    'sqlalchemy', 'pymysql', 'psycopg2', 'mongodb', 'pymongo', 'tinydb', 
    'couchdb', 'redis', 'aioredis', 'aiomysql', 'pony', 'orm', 'dataset', 'datasets', 'peewee'
]

cybersecurity_modules_linux = [
    'cryptography', 'pycryptodome', 'paramiko', 'scapy', 'pyshark', 'dnspython', 'impacket', 
    'requests', 'flask-security', 'django-guardian', 'mitmproxy', 'pyOpenSSL', 'certifi',
    'python-nmap', 'jinja2', 'pyjwt', 'passlib'
]

cloud_computing_modules_linux = [
    'boto3', 'google-cloud', 'azure', 'awscli', 'cloudpickle', 'cloudmesh', 
    'apache-libcloud', 'terraform', 'pulumi', 'ansible', 'kubernetes', 'docker', 
    'docker-compose', 'serverless', 'salt', 'pyinfra', 'cloudinary', 'cloudant', 'troposphere'
]

devops_modules_linux = [
    'ansible', 'jenkins', 'travis-ci', 'git', 'docker', 'docker-compose', 'kubernetes', 
    'vagrant', 'puppet', 'chef', 'salt', 'fabric', 'terraform', 'helm', 'circleci', 'bamboo', 
    'pre-commit', 'pyinfra'
]

big_data_modules_linux = [
    'pyspark', 'hadoop', 'kafka', 'dask', 'ray', 'modin', 'polars', 'koalas', 
    'pyarrow', 'fastparquet', 'h5py', 'tables', 'zarr', 'cudf', 'datashader', 'blaze', 'pandas'
]

bug_bounty_and_ethical_hacking_modules_linux = [
    'scapy', 'impacket', 'paramiko', 'requests', 'beautifulsoup4', 'dnspython', 
    'python-nmap', 'shodan', 'pyshark', 'wappalyzer', 'whois', 'pysmb', 'httplib2', 
    'certifi', 'pycurl', 'idna', 'urllib3', 'cryptography', 
    'pycryptodome', 'pyjwt', 'flask-security', 'django-guardian', 'pyOpenSSL', 'passlib', 'mechanize', 
    'selenium', 'mitmproxy', 'fuzzywuzzy', 'validators', 'recon-ng', 'openpyxl', 'xlrd', 'fping', 
    'traceroute', 'sublist3r', 'arjun', 'nuclei', 'wpscan', 'sqlmap', 'xsstrike', 'fierce', 'masscan', 
    'theHarvester', 'dirsearch', 'amass', 'wfuzz', 'dnsenum', 'dnsrecon', 'metasploit', 'hydra', 
    'nikto', 'whatweb', 'zaproxy', 'burp_suite', 'bruteforce'
]

linux_cybersecurity_tools = {
    "Bug Bounty": [
        "nmap", "dirb", "gobuster", "wfuzz", "nikto", "sublist3r", 
        "amass", "whatweb", "httprobe", "assetfinder", "aquatone", 
        "waybackurls", "hakrawler", "gau", "ffuf", "meg"
    ],
    "Ethical Hacking": [
        "metasploit-framework", "aircrack-ng", "ettercap", "bettercap", 
        "hydra", "john", "hashcat", "sqlmap", "evil-winrm", "medusa", 
        "ncrack", "enum4linux", "smbclient", "crackmapexec", "impacket-scripts"
    ],
    "Web Application Security": [
        "burpsuite", "owasp-zap", "wafw00f", "xsser", "commix", 
        "wpscan", "droopescan", "joomscan", "fimap", "arachni", 
        "nikto", "sqlmap", "dirbuster", "ratproxy", "modsecurity"
    ],
    "Forensics and Malware Analysis": [
        "volatility", "sleuthkit", "autopsy", "foremost", "binwalk", 
        "strings", "radare2", "ghidra", "clamav", "yara", "cuckoo", 
        "hexedit", "fcrackzip", "exiftool", "hashdeep", "bulk_extractor"
    ],
    "Network Security": [
        "wireshark", "tcpdump", "snort", "suricata", "iptables", 
        "tcpreplay", "openvpn", "strongswan", "ettercap", "netsniff-ng", 
        "aircrack-ng", "arp-scan", "hping3", "tshark", "macchanger"
    ],
    "Wireless Security": [
        "airmon-ng", "reaver", "wifite", "kismet", "cowpatty", 
        "hcxdumptool", "hcxtools", "wifi-honey", "eaphammer", 
        "asleap", "fern-wifi-cracker"
    ],
    "Social Engineering": [
        "setoolkit", "social-engineer-toolkit", "evilginx2", "gophish", 
        "maltego", "phishery", "shellphish", "hiddeneye", "weeman", 
        "blackeye"
    ],
    "OSINT": [
        "recon-ng", "theHarvester", "maltego", "spiderfoot", "shodan-cli", 
        "metagoofil", "foospidy", "dmitry", "osrframework", "intelowl", 
        "googlesearch-cli", "amass", "subfinder", "github-dorks"
    ],
    "IoT Security": [
        "bettercap", "iot-checker", "firmadyne", "binwalk", "iot-inspector", 
        "iot-proxy", "iot-penetrator", "shodan-cli", "mdns-scan", 
        "mirai-tools"
    ],
    "Cloud Security": [
        "aws-cli", "gcloud", "azure-cli", "cloudsploit", "prowler", 
        "kube-hunter", "kubesec", "trivy", "steampipe", "pacbot", 
        "skyhigh", "cartography", "threatmapper"
    ],
    "Password Cracking": [
        "hydra", "john", "hashcat", "ophcrack", "fcrackzip", 
        "cewl", "crunch", "maskprocessor", "pack", "rarcrack"
    ],
    "Exploitation Frameworks": [
        "metasploit-framework", "exploitdb", "routersploit", 
        "empire", "beef-xss", "cobaltstrike", "powercat", 
        "powersploit", "linpeas", "winpeas"
    ],
    "Reverse Engineering": [
        "radare2", "ghidra", "ida-free", "hopper", "cutter", 
        "angr", "binaryninja", "apktool", "jd-gui", "smali"
    ],
    "Container Security": [
        "dockscan", "trivy", "grype", "kube-hunter", "dockle", 
        "clair", "anchore-cli", "sysdig", "falco", "container-escape-checker"
    ],
    "Other Tools": [
        "tmux", "screen", "vim", "nano", "curl", "wget", 
        "netcat", "nc", "socat", "rsync", "ssh", "scp", 
        "proxychains", "tor", "zmap", "masscan", "dnsenum"
    ]
}


module_types_linux = [
    None,
    'Basic Modules Linux',
    'Advanced Modules Linux',
    'Science Modules Linux',
    'Computer Vision Modules Linux',
    'Machine Learning Modules Linux',
    'Deep Learning Modules Linux',
    'Full Stack Development Modules Linux',
    'Network Modules Linux',
    'Build Modules Linux',
    'Jupyter Modules Linux',
    'Data Visualization Modules Linux',
    'Database Modules Linux',
    'Cybersecurity Modules Linux',
    'Cloud Computing Modules Linux',
    'DevOps Modules Linux',
    'Big Data Modules Linux',
    'Bug Bounty and Ethical Hacking Modules Linux',
    'linux cybersecurity tools',
]
def install_packages(packages):
    """Install a list of packages using apt."""
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}. Skipping.")

def display_categories():
    """Display available categories."""
    print("\nAvailable Categories:")
    for idx, category in enumerate(linux_cybersecurity_tools.keys(), 1):
        print(f"{idx}. {category}")
    print(f"0. Exit")

def linux_tools_run():
    print("Linux Cybersecurity Tools run")
    while True:
        display_categories()
        choice = input("\nEnter the number of the category to install tools (or '0' to exit): ")
        
        if choice == "0":
            print(f"Thankyou for using me {user} ❤︎")
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(linux_cybersecurity_tools):
                category = list(linux_cybersecurity_tools.keys())[choice - 1]
                tools = linux_cybersecurity_tools[category]
                print(f"\nSelected Category: {category}")
                print(f"Tools to be installed: {', '.join(tools)}")
                confirm = input("Do you want to proceed? (y/n): ")
                if confirm.lower() == 'y':
                    install_packages(tools)
                else:
                    print("Installation cancelled.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")



def is_sudo():
    if os.geteuid() != 0:
        print("This script requires sudo privileges. Relaunching with sudo...")
        try:
            subprocess.check_call(['sudo', sys.executable] + sys.argv)
            sys.exit(0)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to gain sudo privileges: {e}")
            sys.exit(1)
            return False
    else:
        print("Running with sudo privileges.")

def clear():
    return subprocess.run(['clear'],check=True)


def install_vscode_build_tools_and_rust():
    try:
        print("Updating package list...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)

        print("Installing necessary dependencies for VS Code Build Tools...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'wget', 'apt-transport-https', 'software-properties-common'], check=True)

        print("Adding Microsoft GPG key...")
        subprocess.run(['wget', '-qO-', 'https://packages.microsoft.com/keys/microsoft.asc', '|', 'gpg', '--dearmor', '>', '/usr/share/keyrings/microsoft-archive-keyring.gpg'], shell=True, check=True)

        print("Adding VS Code Build Tools repository...")
        subprocess.run(['sudo', 'sh', '-c', 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'], check=True)

        print("Updating package list again...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)

        print("Installing VS Code Build Tools...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'code'], check=True) 

        print("Installing Rust...")
        subprocess.run(['curl', '--proto', '=https', '--tlsv1.2', '-sSf', 'https://sh.rustup.rs', '|', 'sh', '-s', '--', '-y'], shell=True, check=True)

        print("Installation completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False


def log_mod(module_type, module_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Installed {module_name} from {module_type}"
    with open("module_installation_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")


def run():
    if internet() and sys.platform == 'linux':
        upgrade_pip()
        clear()
        banner()
        sys_info()
        lin_py = int(
                    Prompt.ask(
                                "[bold green]Do you want to install linux-based tools (1), or python packages (2):[/]",
                                choices=["1", "2"],  # Valid options
                                show_choices=False,  # Don't show the choices again
                                )
                    )
        if lin_py == 1:
            try:
                is_sudo()
                linux_tools_run()
            except Exception as e:
                print(f"Error occured {e}")

        elif lin_py == 2:
            module_types = [
                'Basic Modules Linux',
                'Advanced Modules Linux',
                'Science Modules Linux',
                'Computer Vision Modules Linux',
                'Machine Learning Modules Linux',
                'Deep Learning Modules Linux',
                'Full Stack Development Modules Linux',
                'Network Modules Linux',
                'Build Modules Linux',
                'Jupyter Modules Linux',
                'Data Visualization Modules Linux',
                'Database Modules Linux',
                'Cybersecurity Modules Linux',
                'Cloud Computing Modules Linux',
                'DevOps Modules Linux',
                'Big Data Modules Linux',
                'Bug Bounty and Ethical Hacking Modules Linux',
                
            ]

            print("\nPlease select the type of modules you want to install:\n")
            for i, module_type in enumerate(module_types, 1):
                    console.print(f"{i}: {module_type}", style="bold white")

            try:
                selected_module_type = int(input("\nEnter the number corresponding to your choice: "))
                if 1 <= selected_module_type <= len(module_types):
                    clear()
                    selected_module_type = module_types[selected_module_type - 1]
                    print(f"\nSelected Module Type: {selected_module_type}")
                    print("Modules:")
                    modules = globals().get(selected_module_type.lower().replace(" ", "_"), [])

                    for i, module in enumerate(modules, 1):
                        print(f"{i}. {module}")

                    install_option = input("Do you want to install all modules in this section? (Yes/No): ").lower()
                    clear()
                    if install_option in ["yes", "y"]:
                        for module in modules:
                            if module == 'dlib':
                                result = ctypes.windll.user32.MessageBoxW(0, "Do you want to continue?", "Alert", 0x40 | 0x1)
                                if result == 1:
                                    print("Module dlib has to be installed after you have installed visual studio build tools")
                                    x = input("Do you want to install VS Build Tools? (y/n): ").lower()
                                    if x == "y":
                                        if install_vscode_build_tools_and_rust():
                                            print("Build tools installed successfully.")
                                        else:
                                            print("Failed to install build tools.")
                                            continue
                                else:
                                    pass

                            if module == 'rust':
                                result = ctypes.windll.user32.MessageBoxW(0, "This Module Requires VSBuild tools.\n Do you want to continue?", "Alert", 0x40 | 0x1)
                                if result == 1:
                                    print("Module rust needs to be installed separately.")
                                    x = input("Do you want to install Rust? (y/n): ").lower()
                                    if x == "y":
                                        if install_vscode_build_tools_and_rust():
                                            print("Rust installed successfully.")
                                        else:
                                            print("Failed to install Rust. Opening the Rust installation webpage.")
                                            webbrowser.open('https://www.rust-lang.org/tools/install')
                                            break
                                else:
                                    pass
                            clear()

                            try:
                                subprocess.run(['pip3', 'install', module, '--break-system-packages'], check=True)
                                log_mod(selected_module_type, module)
                                print(f"{module} installed successfully.")
                            except subprocess.CalledProcessError as e:
                                print(f"Failed to install {module}: {e}")

                        print("\nAll modules installed successfully.")
                        more = input("Do you want to install more? (Yes/No): ")
                        if more.lower() in ["no", "n"]:
                            print("Thank you for using.")
                            sys.exit()
                        elif more.lower() in ["yes", "y"]:
                            run()
                    else:
                        print("Modules:")
                        modules = globals().get(selected_module_type.lower().replace(" ", "_"), [])
                        for i, module in enumerate(modules, 1):
                            print(f"{i}. {module}")

                        module_index = int(input("Enter the number corresponding to the module to install (type '0' to exit): "))

                        if module_index == 0:
                            print("\nReload this program to install new modules of Python.")
                            sys.exit()

                        selected_module = modules[module_index - 1]

                        try:
                            subprocess.run(['pip3', 'install', selected_module, '--break-system-packages'], check=True)
                            log_mod(selected_module_type, selected_module)
                            print(f"{selected_module} installed successfully.")
                        except subprocess.CalledProcessError as e:
                            print(f"Failed to install {selected_module}: {e}")

                        more = input("Do you want to install more? (Yes/No): ")
                        if more.lower() in ["no", "n"]:
                            print("Thank you for using.")
                            sys.exit()
                        elif more.lower() in ["yes", "y"]:
                            run()

                else:
                    print("Invalid selection. Please enter a valid number.")

            except Exception as e:
                print("Error:", e, "\nPlease try again.")
                run()

        else:
            print("Enter 1 or 2 !")
            time.sleep(2)
            clear
            run()

    elif internet() and sys.platform == "win32":
        banner()
        console = Console()
        console.print(" \t This program is designed to run on Linux systems only.", style="bold yellow")
        return
    
    else:
        banner_nointernet()
