
.. image:: _static/image/PYMODINS.png
   :alt: Pymodins Logo
   :align: center
   :width: 200px
   :data-aos: "fade-up"  # Animation when the image comes into view

Welcome to pymodins's Documentation!
=====================================

**Pymodins** is more than just a tool for installing Python modules. 
It’s a guiding hand for newcomers, helping them navigate the complex
landscape of Python development with ease. 
 
With **pymodins**, developers  can  quickly and effortlessly install 
modules tailored to their specific needs, whether it’s basic modules 
for general programming tasks or advanced modules for specialized applications.

This tool can be used on **Windows** as well as **Linux-based Operating Systems**.

**To install with pip:**  
- On Windows, run:  
  ```
  pip install pymodins
  ```
- On Linux, run:  
  ```
  sudo pip3 install pymodins
  ```

**Source Code:**  
The source code is available on [GitHub](https://github.com/Nandhan-ka/pymodins).

**Key Features of pymodins:**

- 🛠️ **Easy Installation:** Install multiple Python modules with a single command.
  
- 📚 **Domain-Specific Packages:** Choose from various domains like Machine Learning, Deep Learning, Data Visualization, and more.

- 🌱 **Beginner-Friendly:** Simplifies the process of setting up Python environments for beginners.

- 🤖 **Automation:** Automates the installation of commonly used Python packages.

- 🔧 **Extensible:** Open to contributions and can be extended to include more modules and features.

- 🚀 **Cross-Platform Support:** Seamlessly works on both Windows and Linux.

- 📊 **Performance Insights:** Gain insights into package installation performance.

- 🛡️ **Security Enhancements:** Secure handling of package installations.

- 📜 **Comprehensive Documentation:** Detailed documentation to guide users.

- 📦 **Package Management:** Manage and install packages with ease.

- 📈 **Error Handling:** Provides detailed error messages to help users troubleshoot issues.

Getting Started
===============

To begin using **pymodins**, follow these simple steps:

1. Install pymodins using pip.
2. Open your command prompt (Administrator mode) or terminal.
3. Run the following command in the command prompt or terminal:

   ```python
   pymodins
   ```
   .. image:: _static/image/run.png
      :alt: Running pymodins
      :align: center
      :width: 60%
      :data-aos: "fade-in"

Commands and Usage
==================

**Basic Commands (if you want to install packages directly by your program):**

1. **Run pymodins:**
   .. code:: python

      >>> import pymodins
      >>> pymodins.run() # Run the pymodins tool and it will guide you through the installation process.

   .. image:: _static/image/run.png
      :alt: Running pymodins
      :align: center
      :width: 60%
      :data-aos: "fade-in"

2. **Install Basic Modules:**
   .. code:: python

      >>> pymodins.install_basic_modules()

   .. image:: _static/image/basic_modules.png
      :alt: Installing Basic Modules
      :align: center
      :width: 60%
      :data-aos: "fade-in"

3. **Install Machine Learning Modules:**
   .. code:: python

      >>> pymodins.install_ml_modules()

4. **Install Data Visualization Modules:**
   .. code:: python

      >>> pymodins.install_data_viz_modules()

Advanced Features
=================

**Domain-Specific Package Installation:**

Pymodins allows you to install packages based on specific domains such as:

- **Machine Learning:** TensorFlow, Scikit-Learn, etc.
- **Data Visualization:** Matplotlib, Seaborn, Plotly.
- **Web Development:** Flask, Django.

**Customization:**

- Modify the configuration file to add your custom package lists.

**Error Handling:**

- Comprehensive error messages to guide users.

Troubleshooting
===============

**Common Issues and Solutions:**

1. **Permission Denied:**
   Ensure you are running the command prompt as an administrator or use `sudo` on Linux.

2. **Package Not Found:**
   Verify your internet connection and package name.

3. **Version Conflicts:**
   Create a virtual environment to avoid conflicts.

This documentation is still a **work in progress**. Stay tuned for more updates!

Indices and Tables
==================

* :ref:`genindex`
