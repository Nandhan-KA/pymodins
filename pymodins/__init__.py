"""
Pymodins - Python Module Installer

This package provides an easy way to install essential Python modules for various tasks,
such as machine learning, deep learning, full-stack development, and more.

Features:
- Cross-platform support for Windows and Linux.
- Installation functions for various categories of Python modules.
"""

import platform

OS = platform.system()

if OS == "Windows":
    from .installer import installer, run
    from .installer import (
        install_basic_modules,
        install_advanced_modules,
        install_build_modules,
        install_computervision_modules,
        install_deeplearning_modules,
        install_fullstack_modules,
        install_jupyter_modules,
        install_machinelearning_modules,
        install_network_modules,
        install_science_modules,
    )
elif OS == "Linux":
    from .linux import  run
else:
    raise OSError(f"Unsupported operating system: {OS}")

__version__ = "2.2.0"

__all__ = [
    "installer",
    "run",
    "install_basic_modules",
    "install_advanced_modules",
    "install_build_modules",
    "install_computervision_modules",
    "install_deeplearning_modules",
    "install_fullstack_modules",
    "install_jupyter_modules",
    "install_machinelearning_modules",
    "install_network_modules",
    "install_science_modules",
]
