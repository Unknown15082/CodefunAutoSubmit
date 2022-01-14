from re import sub
import Tools
import time
from dotenv import load_dotenv
from os import getenv
from requests.exceptions import ConnectionError
load_dotenv()
driver = Tools.setup()
FILE_PATH = getenv("PATH_TO_FOLDER")
language = getenv("LANG", "Python3")
sublist = []

print(f"Preparing for submission of all files in folder {FILE_PATH}")
try:
    sublist = Tools.getlooplist(".py")
except ConnectionError:
    print ("Connection error")
    exit(1)

print(f"Submitting {sublist}")
confirm = input("Proceed? (y/n) ").lower()

if confirm == "y" or confirm == "yes":
    print ("Submitting...")
    for file in sublist:
        try:
            info = Tools.submitfile(driver, f"{FILE_PATH}\{file}")
            print(info)

            if info == 'Not a file to submit':
                continue

            print(f"{file} submitted, waiting for 90 secs")
            time.sleep(90)
        except KeyboardInterrupt:
            print ("Sleep period interrupted, force submitting next file")
        except:
            print (f"Error while submitting {file}")
else:
    print("Aborted")

driver.quit()