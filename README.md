# CodefunAutoSubmit

## Instructions:

1. Download the proper ChromeDriver for your browser from https://chromedriver.chromium.org/downloads
2. Unzip the file and place it in "C:/ChromeDriver/ChromeDriver_V(your current version)"
3. Edit the Tools.py file, line 9 to your version
4. Create a .env file with the following structure:

    CF_USERNAME = (your_codefun_username)

    CF_PASSWORD = (your_codefun_password)

    PATH_TO_FOLDER = (absolute_path_to_the_folder_with_all_your_code)

5. Edit the "tasks" list in AutoSubmit.py to strings corresponding to the tasks you want to submit
6. Run the AutoSubmit.py

## Warnings:

Currently only support C++.