import Tools
import time
from dotenv import load_dotenv
from os import getenv
from requests.exceptions import ConnectionError

load_dotenv()
FILE_PATH = getenv("PATH_TO_FOLDER")
sublist = []

print(f"Preparing for submission of all files in folder {FILE_PATH}")
try:
    sublist = Tools.getlooplist()
except ConnectionError:
    print("Connection error")
    exit(1)

if (len(sublist) == 0):
    print("Nothing to submit")
    exit(0)

print(f"Submitting {sublist}")
confirm = input("Proceed? (y/n) ").lower()

if confirm == "y" or confirm == "yes":
    print("Submitting...")
    driver = Tools.setup()
    for file in sublist:
        try:
            Tools.submitfile(driver, f"{FILE_PATH}\{file}")

            print(f"{file} submitted, waiting for 90 secs")
            time.sleep(90)
        except KeyboardInterrupt:
            print("Sleep period interrupted, force submitting next file")
        except:
            print(f"Error while submitting {file}")
    driver.quit()
else:
    print("Aborted")
