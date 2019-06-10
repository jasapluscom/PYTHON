#!/usr/bin/env python3

'''
selenium_execute_script_sample.py
Example
for python training at www.jasaplus.com
'''

from selenium import webdriver
import time
your_chromium_path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(your_chromium_path)
browser.get("http://localhost/sampleweb")

while True:
    script1 = "setTimeout(function(){ $('#mulai').click();$('#menu_about').click();}, 2000);"
    browser.execute_script(script1)

    script2 = "setTimeout(function(){ $('#mulai').click();$('#menu_services').click();}, 4000);"
    browser.execute_script(script2)

    script3 = "setTimeout(function(){ $('#mulai').click();$('#menu_contact').click();}, 6000);"
    browser.execute_script(script3)

    time.sleep(7)
