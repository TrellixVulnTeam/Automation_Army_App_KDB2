import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
test_case_location = "test_case/test_case.xlsx"

def read_excel():
    read = pd.read_excel(test_case_location)
    for row,column in reader.iterrows():
     sn = column["SN"].values
     test_summary = column["Test_summary"]
     xpath = column["Xpath"]
     action = column["Action"]
     value = column["Value"]
     print(sn,test_summary,xpath,action,value)
     action_defination(sn,test_summary,xpath,action,value)
    print(read)

def action_defination(sn, test_summary,xpath,action,value):
    if action == 'open_browser':
        open_browser(value)
    elif action == 'open_url':
        open_url(value)
    elif action == 'input_text':
        input_text(xpath,value)
    elif action == 'input_text':
        input_text(xpath,value)
    elif action == 'wait':
        wait(value)
    elif action == 'click':
        click(xpath)
    else:
        print(action, "Action not defined")

def open_browser(value):
    global driver
    if value == 'chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
    elif value == 'firefox':
        print("Firefox code here")
    else:
        print(value,"Browser not supported")

def open_url(value):
    driver.get(value)

def input_text(xpath,value):
    driver.find_element(By.XPATH,xpath).send_keys(value)

def input_text(xpath,value):
    driver.find_element(By.Xpath,xpath).send_keys(value)

def click(xpath, value):
    actual_text= driver.find_element(By.Xpath,xpath).send_keys(value)
    try:
        assert actual_text == value

    except AssertionError:
        print("Invalid or Incorrect Password")
    else:
        print("Text matched")

def wait(value):
    time.sleep(value)

if __name__ == "__main__":
    read_excel()