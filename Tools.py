from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
import pyperclip

def setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = options)
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
def query(driver, abspath, lang, id):
    load(driver, "https://codefun.vn/submit", 5)
    login(driver)

    try:
        form_pcode = driver.find_element_by_xpath("//input[@placeholder = 'Pxxxxx']")
        form_lang = Select(driver.find_element_by_xpath("//select[@class = 'form-control']"))
        form_sol = driver.find_element_by_xpath("//textarea")
        form_submit = driver.find_element_by_xpath("//button[@type = 'submit']")
    except:
        return "Error"
    try:
        with open(abspath, 'r') as txt:
            data = txt.read()
    except:
        return "File not found"

    pyperclip.copy(data)

    form_pcode.send_keys(id)
    form_lang.select_by_value(lang)
    form_sol.send_keys(Keys.CONTROL + "v")
    form_submit.click()
    return "Success"

def submitfile(driver, filename):
    if (filename.endswith(".py")):
        return query(driver, filename, "Python3", filename[:-3])
    elif (filename.endswith(".cpp")):
        return query(driver, filename, "C++", filename[:-4])

# Providing only id
def submit(driver, id, lang):
    load_dotenv()
    FILE_PATH = os.getenv("PATH_TO_FOLDER")
    ext = ""
    if (lang == "C++"):
        ext = "cpp"
    elif (lang == "Python3"):
        ext = "py"
    return query(driver, f"{FILE_PATH}/P{id}.{ext}", lang, f"P{id}")
