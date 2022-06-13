import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager

url_location = "SiteList.xlsx"


def read_excelFile():
    reader = pd.read_excel(url_location)
    for row, column in reader.iterrows():
        url = column["URL"]
        site = column["Site Name"]
        serialNumber = column["SN"]
        print(serialNumber, site, url)
        sn = column["SN"]
        # test_summary = column["Test_summary"]
        # xpath = column["Xpath"]
        # action = column["Action"]
        # value = column["Value"]
        # print(sn,test_summary,xpath,action,value)
        # action_defination(sn,test_summary,xpath,action,value)
        print(read)
