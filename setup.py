import platform
from setuptools import setup, find_packages

setup(
    name="pymodins",
    version="2.1.7",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "pymodins_win=pymodins.installer:run",
            "pymodins.creator=pymodins.installer:creator",
            "pymodins_linux=pymodins.linux:installer"
        ],
    },
    author="Nandhan K",
    author_email="developer.nandhank@gmail.com",
    description="Pymodins is more than just a tool for installing Python modules. It's a guiding hand for newcomers, helping them navigate the complex landscape of Python development with ease. With pymodins, developers can quickly and effortlessly install modules tailored to their specific needs, whether it's basic modules for general programming tasks or advanced modules for specialized applications.",
    keywords=[
        "Python Module Installer", 
        "Python Package Installer", 
        "python modules installer", 
        "python package installer", 
        "Nandhan-KA", 
        "PYMODINS", 
        "pymodins",
        "Nandhan K",
        "Nandhan"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Nandhan-KA/pymodins",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Win32 (MS Windows)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    python_requires='>=3.6 ',
    platforms=["win32","linux"],  
)
