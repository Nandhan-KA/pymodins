# setup.py
import platform
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pymodins",
    version="3.0",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "pymodins=pymodins.__main__:main",
            "pymodins-creator=pymodins.installer:creator",
            "pymodins-ui=pymodins.ui:main"
        ],
    },
    author="Nandhan K",
    author_email="developer.nandhank@gmail.com",
    description="A Python module installer for newcomers and seasoned developers.",
    keywords=[
        "Python Module Installer",
        "Python Package Installer",
        "pymodins",
        "Nandhan K",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Nandhan-KA/pymodins",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Environment :: Win32 (MS Windows)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires='>=3.6',
    platforms=["win32", "linux"],  
)
