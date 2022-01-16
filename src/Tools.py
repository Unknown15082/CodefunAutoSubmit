import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from os import getenv, listdir
import requests
import pyperclip

def get_extension(language):
    # C++, Python3, Pascal, NAsm
    if (language == "C++"):
        return "cpp"
    elif (language == "Python3"):
        return "py"
    elif (language == "Pascal"):
        return "pas"
    elif (language == "NAsm"):
        return "s"
    
    raise Exception("Language not found")

def get_language(extension):
    if (extension == "cpp"):
        return "C++"
    elif (extension == "py"):
        return "Python3"
    elif (extension == "pas"):
        return "Pascal"
    elif (extension == "s"):
        return "NAsm"
    raise Exception("Not a valid language")

def setup():
    load_dotenv()
    CHROME_PATH = getenv("CHROME_PATH", "chromedriver.exe")
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
    CF_USERNAME = getenv("CF_USERNAME")
    CF_PASSWORD = getenv("CF_PASSWORD")

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

class Query:
    def __init__(self, driver, abspath, lang, id):
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

        form_pcode.send_keys(id)
        form_lang.select_by_value(lang)
        old_clipboard = pyperclip.paste()
        pyperclip.copy(data)
        form_sol.send_keys(Keys.CONTROL, "v")
        pyperclip.copy(old_clipboard)
        form_submit.click()
    
    def __del__(self):
        pass

def submitfile(driver, filename):

    lang = get_language(filename[filename.rfind('.') + 1 : ])
    Query(driver, filename, lang, filename[:filename.rfind('.')].split("\\")[-1])

# Providing only id
def submit(driver, id, lang):
    load_dotenv()
    FILE_PATH = getenv("PATH_TO_FOLDER")
    ext = get_extension(lang)
    Query(driver, f"{FILE_PATH}\P{id}.{ext}", lang, f"P{id}")

def getaccepted():
    load_dotenv()
    CF_USERNAME = getenv("CF_USERNAME")
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
        if (abs(submission["score"] - submission["maxScore"]) < 0.000000001):
            accepted.append(submission["problem"]["code"])
    return accepted

def retrieveSubmission(driver, subID, code, lang):
    load(driver, f"https://codefun.vn/submissions/{subID}", 3)
    login(driver)

    load_dotenv()
    PATH = getenv("PATH_TO_FOLDER")

    try:
        rawcode = driver.find_element_by_xpath("//code").text
        language = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[1]/div/div[2]/ul/li[3]/b").text
    except:
        return "No code found"

    print(language)

    if (language != lang):
        return

    with open(f"{PATH}/{code}.{get_extension(lang)}", "w+") as f:
        f.write(rawcode)

def retrieveAllAC():
    load_dotenv()
    CF_USERNAME = getenv("CF_USERNAME")

    response = requests.get(f"https://codefun.vn/api/users/{CF_USERNAME}/stats?")
    data = response.json()["data"]

    sublist = []

    for problem in data:
        if (abs(problem["score"] - problem["maxScore"]) < 0.000000001):
            sublist.append([problem["submissionId"], problem["problem"]["code"]])

    return sublist


# ext is filter for file extension
def getlooplist():
    load_dotenv()
    FILE_PATH = getenv("PATH_TO_FOLDER")
    ext = get_extension(getenv("LANGUAGE"))
    aclist = getaccepted()
    # print(aclist)
    sublist = []
    for filename in listdir(FILE_PATH):
        if (filename.endswith(ext) and filename.split(".")[0] not in aclist and not filename.startswith("pass")):
            print(filename.split(".")[0])
            sublist.append(filename)
    return sublist