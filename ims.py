
import os
import glob

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def capture_image():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
   # s = Service('./chromedriver')
    s = Service(ChromeDriverManager().install()) #It will install chromedriver in runtime,
    # DeprecationWarning: executable_path has been deprecated, please pass in a Service object
    driver = webdriver.Chrome(service=s)
    driver.get('http://imswebpos.com:7050/#/pages/dashboard.asmx')
    time.sleep(3)
    full_name = driver.find_element(By.XPATH,'(//input[contains(@id,"ctl00_ContentPlaceHolder1_txt")])[2]')
    full_name.send_keys("Ram Khadka")
    time.sleep(3)

if __name__ == '_main_':
    capture_image()