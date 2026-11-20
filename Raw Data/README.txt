RETAIL SALES ANALYSIS - SETUP GUIDE
==================================

This guide explains how to install Python, install the required libraries,
and run the retail sales analysis project.


1. INSTALL PYTHON
-----------------

If Python is not installed, download it from the official Python website:
https://www.python.org/downloads/

On Windows, run the installer and check "Add Python to PATH" before installing.
After installation, close and reopen PowerShell or Command Prompt.

Python's Windows installation guide:
https://docs.python.org/3/using/windows.html

Note: pip installs Python libraries. It does not install Python itself.


2. CHECK PYTHON INSTALLATION
----------------------------

Windows PowerShell or Command Prompt, try:

    py --version

If that command is not recognized, try:

    python --version

macOS or Linux:

    python3 --version


3. INSTALL THE PROJECT LIBRARIES
--------------------------------

This version of the project uses pandas and matplotlib.

Windows, if the py command works:

    py -m pip install pandas matplotlib

Windows, if python works but py does not:

    python -m pip install pandas matplotlib

macOS or Linux:

    python3 -m pip install pandas matplotlib


4. PUT THE DATASET IN PLACE
---------------------------

The dataset must be named exactly:

    retail_sales_dataset.csv

Put it in either of these locations:

    - In the same folder as retail_sales_analysis.py
    - In a folder named Raw Data next to the script's folder


5. RUN THE PROJECT
------------------

First, use PowerShell or Command Prompt to move into the folder containing
retail_sales_analysis.py. For example:

    cd "C:\Users\YourName\Downloads\Python File"

Windows, try:

    py retail_sales_analysis.py

If py is not recognized but python works:

    python retail_sales_analysis.py

macOS or Linux:

    python3 retail_sales_analysis.py

The summary tables and charts will be saved in a folder named
analysis_output beside the Python script.


COMMON ERRORS
-------------

"python is not recognized" or "py is not recognized"
    Install Python from https://www.python.org/downloads/ . On Windows,
    select "Add Python to PATH" in the installer. Then reopen the terminal.

"No module named pandas" or "No module named matplotlib"
    Install the libraries using the command in section 3. Use the same Python
    command (py, python, or python3) to install packages and run the script.

"pip is not recognized"
    Run pip through Python instead: py -m pip, python -m pip, or
    python3 -m pip, depending on which Python command works on your system.

"FileNotFoundError" for retail_sales_dataset.csv
    Check the spelling of the CSV filename and put it in one of the locations
    described in section 4.
