import os
import getpass
import sys
import urllib.request
from datetime import datetime
from rich.console import Console

user = getpass.getuser()

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


def clear():
    return os.system('cls')


def log_mod(module_type, module_name, python_folder):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Installed {module_name} from {module_type} in {python_folder}"
    with open("module_installation_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")


# Module Lists
basic_modules = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'requests', 'beautifulsoup4', 'seaborn', 'tqdm', 'docutils', 'pyyaml', 'python-dotenv', 'pillow',
]

advanced_modules = [
    'functools', 'logging', 'argparse', 'asyncio', 'collections', 'contextlib', 'dataclasses', 'pytz', 'pathlib', 'typing_extensions',
]

science_modules = [
    'numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-image', 'statsmodels', 'sympy', 'networkx', 'biopython',
]

computer_vision_modules = [
    'opencv-python', 'Pillow', 'imageio', 'pytesseract', 'pyautogui', 'pyzbar', 'dlib'
]

machine_learning_modules = [
    'scikit-learn', 'tensorflow', 'keras', 'xgboost', 'lightgbm', 'catboost', 'shap',
]

deep_learning_modules = [
    'torch', 'pytorch-lightning', 'transformers', 'fastai', 'keras-rl', 'tensorboard',
]

full_stack_development_modules = [
    'flask', 'django', 'fastapi', 'express', 'sqlalchemy', 'django-orm', 'mongodb', 'mongoose', 'react', 'vue', 'angular', 'jquery', 'bootstrap', 'tailwindcss', 'swagger', 'postman', 'git', 'github-cli', 'docker', 'docker-compose', 'kubernetes', 'nginx', 'apache', 'oauthlib', 'python-social-auth', 'passport', 'pytest', 'jest', 'ansible', 'jenkins', 'travis-ci', 'prometheus', 'grafana', 'elk-stack', 'redis', 'celery', 'graphql', 'socket.io',
]

network_modules = [
    'socket', 'http.client', 'urllib', 'requests', 'socketIO-client', 'websockets', 'http.server', 'flask', 'django',
]

build_modules = [
    'pep517', 'setuptools', 'build', 'wheel', 'pytoml', 'cmake'
]
jupyter_modules = [
    'jupyter'
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
    
if __name__ == '__main__':
    run()
