import Tools
import time
from dotenv import load_dotenv
from os import getenv
load_dotenv()
driver = Tools.setup()
FILE_PATH = getenv("PATH_TO_FOLDER")
language = getenv("LANG", "Python3")

print(f"Preparing for submission of all files in folder {FILE_PATH}")
sublist = Tools.getlooplist(".py")
if (sublist == "Error"):
    print("Please check your internet connection")
    exit(0)
print(f"Submitting {sublist}")
confirm = input("Proceed? (y/n)").lower()

if (confirm == "y"):
    for file in sublist:
        exitcode = Tools.submitfile(driver, f"{FILE_PATH}/{file}")
        if (exitcode == "Success"):
            time.sleep(90)
else:
    print("Aborted")