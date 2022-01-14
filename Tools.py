import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
import pyperclip
import requests
import time
def setup():
    load_dotenv()
    CHROME_PATH = os.getenv("CHROME_PATH", "chromedriver.exe")
    options = webdriver.ChromeOptions()
    # Ignore Bluetooth error messages
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = CHROME_PATH, options = options)
    return driver

def load(driver, url, wtime):
    driver.get(url)
    driver.implicitly_wait(wtime)

def login(driver):
    load_dotenv()
    CF_USERNAME = os.getenv("CF_USERNAME")
    CF_PASSWORD = os.getenv("CF_PASSWORD")

    try:
        form_user = driver.find_element_by_xpath("//input[@placeholder = 'Username']")
        form_pass = driver.find_element_by_xpath("//input[@placeholder = 'Password']")
        form_login = driver.find_element_by_xpath("//button[@type = 'submit']")
    except:
        return "Error"

    form_user.send_keys(CF_USERNAME)
    form_pass.send_keys(CF_PASSWORD)
    form_login.click()

    return "Success"
class query:
    def __init__(self, driver, abspath, lang, id):
        self.drv = driver
        load(driver, "https://codefun.vn/submit", 5)
        login(driver)

        try:
            form_pcode = driver.find_element_by_xpath("//input[@placeholder = 'Pxxxxx']")
            form_lang = Select(driver.find_element_by_xpath("//select[@class = 'form-control']"))
            form_sol = driver.find_element_by_xpath("//textarea")
            form_submit = driver.find_element_by_xpath("//button[@type = 'submit']")
        except:
            raise Exception("Selenium Error")
        try:
            with open(abspath, 'r') as txt:
                data = txt.read()
        except:
            raise Exception("File not found")

        pyperclip.copy(data)

        form_pcode.send_keys(id)
        form_lang.select_by_value(lang)
        form_sol.send_keys(Keys.CONTROL + "v")
        form_submit.click()
    def __del__(self):
        pass

def submitfile(driver, filename):
    if (filename.endswith(".py")):
        query(driver, filename, "Python3", filename[:-3].split("\\")[-1])
    elif (filename.endswith(".cpp")):
        query(driver, filename, "C++", filename[:-4])

# Providing only id
def submit(driver, id, lang):
    load_dotenv()
    FILE_PATH = os.getenv("PATH_TO_FOLDER")
    ext = ""
    if (lang == "C++"):
        ext = "cpp"
    elif (lang == "Python3"):
        ext = "py"
    query(driver, f"{FILE_PATH}\P{id}.{ext}", lang, f"P{id}")

def getaccepted():
    load_dotenv()
    CF_USERNAME = os.getenv("CF_USERNAME")
    # json scheme:
    # {
    # "data": [
    #         {
    #         "problem": {
    #             "id": 274,
    #             "code": "P10001",
    #             "name": "Trò chơi của Shi-ura"
    #         },
    #         "submissionId": 2375281,
    #         "score": 100,
    #         "maxScore": 100,
    #         "submitTime": 1633103943
    #         }
    #     ]
    # }
    accepted = []
    # try:
    response = requests.get(f"https://codefun.vn/api/users/{CF_USERNAME}/stats?")
    json_data = json.loads(response.text)["data"]
    
    for submission in json_data:
        if (submission["score"] == submission["maxScore"]):
            accepted.append(submission["problem"]["code"])
    return accepted

# ext is filter for file extension
def getlooplist(ext):
    load_dotenv()
    FILE_PATH = os.getenv("PATH_TO_FOLDER")
    aclist = getaccepted()
    # print(aclist)
    sublist = []
    for filename in os.listdir(FILE_PATH):
        if (filename.endswith(ext) and filename.split(".")[0] not in aclist and not filename.startswith("pass")):
            print (filename.split(".")[0])
            sublist.append(filename)
    return sublist