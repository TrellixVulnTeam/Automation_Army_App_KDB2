from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from webdriver_manager.core import driver


class DemoDropdownSingleSelect:

def open_url():
    s = Service(ChromeDriverManager().install())  # It will install chromedriver in runtime,
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('http://imsnepal.com/nepalisenapasal/#/login')
    driver.find_element(By.XPATH, '//input[@id="inputEmail3"]').send_keys("admin_army")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="inputPassword3"]').send_keys("army@666")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    """dropdown = driver.find_element(By.XPATH, '//li[@title="Masters"]//ul[@class="al-sidebar-sublist"]')
    dd = Select(dropdown)

    dd.select_by_index(1)
    time.sleep(3)

    dd.select_by_visible_text("Customer Register List")
    time.sleep(2)

    dd.select_by_value("ba-sidebar-sublist-item")
    time.sleep(3)

    #driver.find_element(By.XPATH, '////ba-page-top/div').click()
    #time.sleep(2)
    #driver.find_element(By.XPATH, '//class[@style="al-sidebar-sublist")]').click()
    #time.sleep()
    #driver.find_element(By.XPATH, '//a[contains(@href, "white-space: initial")]').click()
    #time.sleep(2)
    #river.find_element(By.XPATH, '//a[span style(@Customer Register List="")]').click()
    #time.sleep(2)
    #driver.find_element(By.XPATH, '//a[span style(@customer. Register List ="')
    #time.sleep(2)

dddemo = DemoDropdownSingleSelect()
dddemo.demo_dropedown()"""

    driver.find_element(By)

# search_box = driver.find_element()

if __name__ == '__main__':
        open_url()
