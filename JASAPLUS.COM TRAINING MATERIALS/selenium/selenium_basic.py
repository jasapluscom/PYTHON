#!/usr/bin/env python3

'''
selenium_basic.py

Basic Selenium Example
for python training at www.jasaplus.com
'''

from selenium import webdriver
import time
your_chromium_path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(your_chromium_path)
browser.get("http://localhost/sampleweb")
time.sleep(8)
html_source = browser.page_source
print("html_source : ")
print(html_source)
