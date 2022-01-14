import os
import webbrowser
def main():
    try:
        import time
        from dotenv import load_dotenv
        import json
        from selenium import webdriver
        import requests
    except ImportError:
        print("Installing dependencies...")
        os.system("pip install -r requirements.txt")
    
    username = input("What is your Codefun username?\n")
    pwd = input("What is the password?\n")
    
    filepath = input("What is the absolute path to the folder containing your code?\n").replace("/","\\")
    if (filepath.endswith("\\")):
        filepath = filepath[:-1]
    
    lang = input("What is the default submitting language? (C++/Python3/Pascal/NAsm)\n")
    
    chromedriverpath = input("What is the path to your chromedriver.exe file? (Type NA if you don't have chromedriver.exe)\n")
    while chromedriverpath == "NA":
        print ("Redirecting to https://chromedriver.chromium.org/downloads")
        webbrowser.open_new_tab("https://chromedriver.chromium.org/downloads")
        chromedriverpath = input("What is the path to your chromedriver.exe file?\n")
    with open(".env", "w") as f:
        f.write(f"CF_USERNAME = {username}\n")
        f.write(f"CF_PASSWORD = {pwd}\n")
        f.write(f"PATH_TO_FOLDER = {filepath}\n")
        f.write(f"LANGUAGE = {lang}\n")
        f.write(f"CHROME_PATH = {chromedriverpath}\n")

    print("Success")

    # TODO: Check for errors

if __name__ == "__main__":
    main()