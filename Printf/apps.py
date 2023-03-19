from django.apps import AppConfig
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
        
from django.apps import AppConfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class PrintfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Printf'
    def ready(self):
        chrome_options = webdriver.ChromeOptions()
        

        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        global browser;
        browser = webdriver.Chrome(executable_path=r"C:\Users\ANKIT\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
        
        url = 'https://web.whatsapp.com/'


        browser.maximize_window()

        browser.get(url)
#         # file_path = r"C:\Users\ANKIT\Desktop\automation\bb.docx"

# # Set the message you want to send
#         message = "Here's the file you requested."

# # Set the phone number of the recipient
#         phone_number = "+917979959844"

# # Set the time at which you want to send the message (24-hour format)
        send_hour = 13
        send_min = 30


# # Set Chrome options to disable USB devices


