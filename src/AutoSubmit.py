import Tools as Tools
from os import getenv
import time

tasks = ["001"]
language = getenv("SUBMITLANGUAGE", "Python3")
driver = Tools.setup()

for i in tasks:
    try:
        Tools.submit(driver, i, language)
        print(f"{i} submitted, waiting for 90 secs")
        time.sleep(90)
    except KeyboardInterrupt:
        print ("Sleep period interrupted, force submitting next file")
    except:
        print (f"Error while submitting {i}")
driver.quit()