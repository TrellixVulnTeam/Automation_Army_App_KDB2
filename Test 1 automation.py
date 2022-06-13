from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
#demo#
def open_url():
    s = Service(ChromeDriverManager().install())  # It will install chromedriver in runtime,
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('http://imswebpos.com:7050/#/pages/login')
    driver.find_element(By.XPATH, '//input[@formcontrolname="username"]').send_keys("Puja")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("12345")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[contains(text(),"Sign In")]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//span[contains(.,"Masters")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"Product Master")]').click()
    time.slep(2)

    driver.find_element(By)

    #search_box = driver.find_element()

if __name__ == '__main__':
    open_url()



