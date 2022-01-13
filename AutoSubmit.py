import Tools
import time

tasks = ["001"]
driver = Tools.setup()

for i in tasks:
    exitcode = Tools.submit(driver, i)
    if (exitcode == "Success"):
        time.sleep(90)