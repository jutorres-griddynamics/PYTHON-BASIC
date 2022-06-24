"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.

    https://blog.jovian.ai/web-scraping-yahoo-finance-using-python-7c4612fab70c


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

from selenium import webdriver
import time
def get_table_rows(driver):
    """Get number of rows available on the page """
    tablerows = len(driver.find_elements(By.XPATH, value='//*[@id="scr-res-table"]/div[1]/table/tbody/tr'))
    return tablerows

def get_table_header(driver):
    """Return Table columns in list form """
    header = driver.find_elements(By.TAG_NAME, value= 'th')
    header_list = [item.text for index, item in enumerate(header) if index < 10]
    return header_list

def get_driver(url):
    """Return web driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="/Users/julitorresma/Downloads/chromedriver",
                              chrome_options=options)
    driver.get(url)

    return driver

driver = get_driver('https://finance.yahoo.com/cryptocurrencies')
print(driver.title)
header = driver.find_elements(By.TAG_NAME, value= 'th')
print(header[0].text)
print(header[2].text)

txt=driver.find_element(By.XPATH, value='//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]').text

print(get_table_rows(driver))