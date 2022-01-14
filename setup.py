def main():
    username = input("What is your Codefun username?\n")
    pwd = input("What is the password?\n")
    filepath = input("What is the absolute path to the folder containing your code?\n")
    lang = input("What is the default submitting language? (C++/Python3/Pascal/NAsm)\n")
    chromedriverpath = input("What is the path to your chromedriver.exe file?\n")

    with open(".env", "w+") as f:
        f.write(f"CF_USERNAME = {username}\n")
        f.write(f"CF_PASSWORD = {pwd}\n")
        f.write(f"PATH_TO_FOLDER = {filepath}\n")
        f.write(f"LANG = {lang}\n")
        f.write(f"CHROME_PATH = {chromedriverpath}\n")

    print("Success")

    # TODO: Check for errors

if __name__ == "__main__":
    main()