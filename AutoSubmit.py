import Tools
import time

tasks = ["001"]
language = "Python3" # Or C++
driver = Tools.setup()

for i in tasks:
    exitcode = Tools.submit(driver, i, language)
    if (exitcode == "Success"):
        time.sleep(90)