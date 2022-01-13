from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import pyperclip

def setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path = "C:/ChromeDriver/ChromeDriver_V97/chromedriver.exe", options = options)
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

def submit(driver, id):
    '''
    Currently default to C++.
    '''

    load(driver, "https://codefun.vn/submit", 5)
    login(driver)

    try:
        form_pcode = driver.find_element_by_xpath("//input[@placeholder = 'Pxxxxx']")
        form_sol = driver.find_element_by_xpath("//textarea")
        form_submit = driver.find_element_by_xpath("//button[@type = 'submit']")
    except:
        return "Error"

    load_dotenv()
    FILE_PATH = os.getenv("PATH_TO_FOLDER")

    try:
        with open(f"{FILE_PATH}/P{id}.cpp", 'r') as txt:
            data = txt.read()
    except:
        return "File not found"

    pyperclip.copy(data)

    form_pcode.send_keys(f"P{id}")
    form_sol.send_keys(Keys.CONTROL + "v")
    form_submit.click()

    return "Success"