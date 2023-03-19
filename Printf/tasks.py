from celery import shared_task
from selenium import webdriver
import time
import os



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from .apps import PrintfConfig,browser

from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

import os

from celery import Celery


@shared_task
def test(file_path,details):
    browser.execute_script("window.open('');")

# # Switch to the new tab

# # Switch to the new tab
    browser.switch_to.window(browser.window_handles[-1])
    url = 'https://web.whatsapp.com/'


    browser.get(url)
    file_path = file_path

# # Set the message you want to send

# # Set the phone number of the recipient
    phone_number = "Printf"

# # Set the time at which you want to send the message (24-hour format)
    send_hour = 13
    send_min = 30


# # Set Chrome options to disable USB devices

# # Wait for the user to scan the QR code
    time.sleep(30)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

# # # Find the element using xpath
    search_box = browser.find_element("xpath","//div[@contenteditable='true'][@data-tab='3']")

# # # Use the element to perform actions
    search_box.send_keys(phone_number)

# # Select the recipient's contact by phone number

    
    search_box.send_keys(u'\ue007')
    time.sleep(2)

# # Click the attachment button
    attachment_button = browser.find_element("xpath", '//div[@title="Attach"]')
    attachment_button.click()
    time.sleep(2)

# # Click the document option
    document_option = browser.find_element("xpath", "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input"
)
    document_option.send_keys(file_path)
    time.sleep(2)

# # Send the file with the specified message
    message_box = browser.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/p')
    message_box.send_keys(details)
    
    send_button = browser.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')
    send_button.click()
    time.sleep(10)
    return None
@shared_task
def done(message1):
    browser.execute_script("window.open('');")

# # Switch to the new tab

# # Switch to the new tab
    browser.switch_to.window(browser.window_handles[-1])
    url = 'https://web.whatsapp.com/'


    browser.get(url)
    file_path = r"C:\Users\ANKIT\Desktop\automation\bb.docx"

# # Set the message you want to send
    

# # Set the phone number of the recipient
    phone_number = "Printf"

# # Set the time at which you want to send the message (24-hour format)
    send_hour = 13
    send_min = 30


# # Set Chrome options to disable USB devices

# # Wait for the user to scan the QR code
    time.sleep(10)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

# # # Find the element using xpath
    search_box = browser.find_element("xpath","//div[@contenteditable='true'][@data-tab='3']")

# # # Use the element to perform actions
    search_box.send_keys(phone_number)

# # Select the recipient's contact by phone number

    
    search_box.send_keys(u'\ue007')
    time.sleep(2)
# ------------------------------------------------------------------------------------
#  Send Success Message
    message_boxs = browser.find_element("xpath", '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_boxs.send_keys(message1)
    

    time.sleep(2)

    submit = browser.find_element("xpath", '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    submit.click()


    return None

