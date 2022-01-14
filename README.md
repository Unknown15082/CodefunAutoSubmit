# CodefunAutoSubmit

## Installation:

1. Download the proper ChromeDriver for your browser from https://chromedriver.chromium.org/downloads
2. Unzip the file and place it in the running folder (refer to the next step for more details)
3. Create a .env file in the running folder with the following structure:
    CF_USERNAME = (your_codefun_username)
    CF_PASSWORD = (your_codefun_password)
    PATH_TO_FOLDER = (absolute_path_to_the_folder_with_all_your code)
    LANG = (language_used) (Python3 and C++ are currently supported) (optional, defaults to Python3)
    CHROME_PATH = (full_path_to your_distribution_of_chromedriver.exe) (optional, defaults to running path or the chromedriver exe specified in PATH)

4. If you don't have the libraries used, run "pip install -r path/to/requirements.txt" (subsitute with your own path)

## Quick Start Guide
### Specify a list of problems to periodically submit
1. Edit the "tasks" list in AutoSubmit.py to strings corresponding to the tasks you want to submit
2. Run the AutoSubmit.py

### Scan a specified folder for problems that have yet to receive an accepted verdict and submit them
1. Rename all unfinished code file in the specified folder with "pass{name}" (For example: passP001.py)
2. Run the AutoSubmitAll.py file
3. Follow the on-screen instruction to proceed with the submission process

## Notes:
Currently only support C++ and Python3.
Make sure that the information provided in the .env file is correct (otherwise it's undefined behavior)
Please use this tool in accordance with Codefun's rules. The developers and contributors strongly discourage the use of this tool for plagiarism.
