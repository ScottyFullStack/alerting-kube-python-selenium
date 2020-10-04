#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get("http://192.168.99.121:30880")

hello_text = driver.find_element(By.XPATH, "//*[text()='Hello, World!']")
print('Success: {}'.format(hello_text))
driver.close()