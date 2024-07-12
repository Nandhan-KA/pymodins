import platform
from setuptools import setup, find_packages

if platform.system() == "Windows":
    setup(
        name="pymodins",
        version="2.1.6",
        packages=find_packages(),
        install_requires=[
            "rich"
        ],
        entry_points={
            "console_scripts": [
                "pymodins=pymodins.installer:run",
                "pymodins.creator=pymodins.installer:creator"
            ],
        },
        author="Nandhan K",
        author_email="nandhan2003alamelu@gmail.com",
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
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
        python_requires='>=3.6',
        platforms=["win32"],  
    )
else:
    raise RuntimeError("This program is designed to run on Windows systems only.")
