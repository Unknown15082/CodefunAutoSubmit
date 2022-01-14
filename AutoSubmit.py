import Tools
import time

tasks = ["001"]
language = "Python3" # Or C++
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