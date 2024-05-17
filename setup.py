from setuptools import setup, find_packages

setup(
    name="pymodins",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "pymodins=pymodins.installer:main",
        ],
    },
    author="Nandhan K",
    author_email="nandhan2003alamelu@gmail.com ",
    description="A module to install various Python packages.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Nandhan-KA/pymodins",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

