#!/usr/bin/env python3

'''
FindElement.py
Selenium Example
for python training at www.jasaplus.com
'''

from selenium import webdriver
import time

def _start_view_menu(browser):
    try:
        start = browser.find_element_by_id("mulai")
        start.click()
        time.sleep(1)
    except:
        raise

your_chromium_path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(your_chromium_path)
browser.get("http://localhost/sampleweb")
time.sleep(1)


_start_view_menu(browser)
portfolios = browser.find_elements_by_class_name("js-scroll-trigger")
for port in portfolios:
    if port.text == "Portfolio":
        port.click()


'''
#find element by name sample
linkz = browser.find_element_by_name("linkz")
print(linkz.text)
print(linkz.get_attribute('innerHTML'))

#find element by id sample
_start_view_menu(browser)
about = browser.find_element_by_id("menu_about")
if about != None:
    about.click()

#find element by link text sample
_start_view_menu()
el1 = browser.find_element_by_link_text('Services')
if el1 != None:
    el1.click()
el2 = browser.find_element_by_partial_link_text("folio")
if el2 != None:
    el2.click()


#find element by tag name example
_start_view_menu(browser)
links = browser.find_elements_by_tag_name('a')
for link in links:
    if link.text == "About":
        link.click()
        break


'''
