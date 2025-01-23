# pymodins/__main__.py
import platform
from pymodins.installer import run as windows_installer
from pymodins.linux import run as linux_installer

def main():
    current_platform = platform.system().lower()
    if current_platform == "windows":
        windows_installer()
    elif current_platform == "linux":
        linux_installer()
    else:
        print(f"Unsupported platform: {current_platform}")

if __name__ == "__main__":
    main()
