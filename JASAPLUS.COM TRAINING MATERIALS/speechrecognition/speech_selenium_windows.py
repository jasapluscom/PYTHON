#!/usr/bin/env python3

'''
speech_selenium_windows.py
Example
for python training at www.jasaplus.com
'''

from selenium import webdriver
from gtts import gTTS
import time, os

data = ""
data_prev = ""

def speech(data):
    try:
        tts = gTTS(text=data, lang='en', slow=True).save("tmp.mp3")
        cmd = "vlc --intf dummy tmp.mp3 vlc://quit"
        pipe = os.popen(cmd)
    except:
        raise

def setopt():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 1
    })
    return opt

opti = setopt()
browser = webdriver.Chrome(chrome_options = opti)
browser.get("http://localhost/webspeech/")
browser.set_window_position(800, 370)
browser.set_window_size(520, 350)
count = 0
while True:
    data = browser.find_element_by_id("data").get_attribute("value");
    if data != "None":
        data = data.strip()
        if (data != data_prev) and (len(data) > 0):
            data_prev = data
            print(data)
            speech(data)
            count = 0
    time.sleep(1)
    count+=1
    if (count > 15):
        startme = browser.find_element_by_id("startme")
        if startme != None:
            startme.click()
