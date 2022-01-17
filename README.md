# CodefunAutoSubmit

## Installation:

1. Download the proper ChromeDriver for your browser from https://chromedriver.chromium.org/downloads
2. Unzip the file and place it in the running folder or another folder
3. Run the setup.py file
4. If you don't have the libraries used, run "pip install -r path/to/requirements.txt" (substitute with your own path)

## Quick Start Guide
### Specify a list of problems to periodically submit
1. Edit the "tasks" list in AutoSubmit.py to strings corresponding to the tasks you want to submit
2. Run the AutoSubmit.py

### Scan a specified folder for problems that have yet to receive an accepted verdict and submit them
1. Rename all unfinished code file in the specified folder with "pass{name}" (For example: passP001.py)
2. Run the AutoSubmitAll.py file
3. Follow the on-screen instruction to proceed with the submission process

## Notes:
Currently only support C++, Python3, Pascal and NAsm.

While this tool currently only supports Windows, any pull requests about support for Ubuntu and other OSes are welcomed

Make sure that the information provided in the setup.py file is correct (otherwise it's undefined behavior)

Please use this tool in accordance with Codefun's rules. The developers and contributors strongly discourage the use of this tool for plagiarism.
