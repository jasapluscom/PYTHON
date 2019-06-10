#!/usr/bin/env python3

'''
input_modif.py
Example
for python training at www.jasaplus.com
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
your_chromium_path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(your_chromium_path)
browser.get("https://www.google.com")
time.sleep(1)
search = browser.find_element_by_name("q")
search.clear()
search.send_keys("hacker")
search.send_keys(Keys.RETURN)
