import Tools
from dotenv import load_dotenv
from os import getenv

driver = Tools.setup()

load_dotenv()
LANG = getenv("LANGUAGE")

sublist = Tools.retrieveAllAC()
for p in sublist:
    Tools.retrieveSubmission(driver, p[0], p[1], LANG)