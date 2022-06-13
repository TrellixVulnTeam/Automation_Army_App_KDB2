from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def open_url():
    s = Service(ChromeDriverManager().install())  # It will install chromedriver in runtime,
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('http://imsnepal.com:8080/test/User/Login?ReturnUrl=%2ftest%2f')
    driver.find_element(By.XPATH, '//input[@id="UNAME"]').send_keys("Puja")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys("puja123")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    time.sleep(2)

    driver.find_element(By)

    if __name__ == '_main_':
        open_url()



