#!/usr/bin/env python3

import os, sys, time, inspect, codecs,signal, threading, requests, math, re
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from bs4 import BeautifulSoup
import config

browser = 0
page_switch = 0
current_log_path = ""
thread_number = 3
global_ci_user_lists = []

def RandomUa():
    try:
        selected_ua = "?"
        ua_lists = []
        ua_lists.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
        ua_lists.append("Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0")
        ua_lists.append("Mozilla/5.0 (Windows NT 6.1; rv:55.0) Gecko/20100101 Firefox/55.0")
        total = len(ua_lists)
        rand_num = randint(0, total - 1)
        selected_ua = ua_lists[rand_num].strip()
        return selected_ua
    except:
        print("[+] Problem in RandomUA")
        #raise
        pass
    
def InitDir():
    try:
        global current_log_path
        
        if os.path.exists('/log.txt') == False:
            os.system("touch log.txt")
        
        os.system("echo '' > log.txt")
    
    except Exception as e:
        print("[+] Problem in InitDir")
        raise e

def BrowserWaitForPageLoad(timeout=4):
    global browser
    try:
        old_page = browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(timeout).until(staleness_of(old_page))
    except Exception as e:
        print(str(e))
        time.sleep(1)
        #raise
        pass
    
def Init():
    try:
        global browser
        print("[+] init browser")
        ua = "?"
        ua = RandomUa()
        opts = webdriver.ChromeOptions()
        #opts.add_argument('headless')
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = { 'browser':'ALL' }
        opts = webdriver.ChromeOptions()
        opts.add_argument('--user-agent=' + ua)
        opts.add_experimental_option("detach", True)
        opts.add_experimental_option("useAutomationExtension", False)
        opts.add_experimental_option("excludeSwitches",["enable-automation"])
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        opts.add_experimental_option("prefs",prefs)
        prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
        opts.add_experimental_option("prefs", prefs)
        opts.add_argument('--disable-notifications')

        #opts.add_argument("--disable-infobars")
        #opts.add_argument("--kiosk")
        opts.add_argument("--start-maximized")
        opts.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(chrome_options=opts)
        url = "https://github.com/search?l=PHP&p=1&q=followers%3A%3E%3D1000+filename%3ACodeIgniter.php+followers%3A%3E1000+language%3APHP+language%3APHP&ref=advsearch&type=Users"
        browser.get(url)
    except Exception as e:
        print("[-] problem occurs, please re - run the script or ask the developer to fix")
        raise e

        
def InjectJsFile(file_name):
    try:
        global browser
        print("[+] injecting web")
        with open('lib/' +  file_name, 'r') as jsf: 
            js = jsf.read()
            try:
                browser.execute_script(js)
            except Exception as e:
                print("[-] problem in execute script")
                #raise e
                pass
        time.sleep(1)
    except Exception as e:
        print("[-] problem in inject js file")
        #raise e
        pass

def WaitForFingerprint(page_fingerprint_to_find = ""):
    try:
        global browser
        print("[+] waiting for fingerprint : " + page_fingerprint_to_find)
        found = 0
        source = ""
        while found == 0:
            BrowserWaitForPageLoad(3)
            source = browser.page_source
            if source.find(page_fingerprint_to_find) != -1:
                found = 1
                break
            time.sleep(1)
    except Exception as e:
        print("[-] problem in WaitForFingerprint ... no worry continuing")
        #raise
        pass
    
def LogMsg(data):
    try:
        global current_log_path
        
        print("[+] LogMsg mode :" + data)
        data = data.strip()
        print("[-] mode log not found : " + data)
        
    except Exception as e:
        raise e
        #pass      

def CollectUsers(maxpage):
    try:
        global browser
        user_lists = []
        print("[+] collect users")
        for p in range(1, int(maxpage) + 1):
            if p > 1:
                url = "https://github.com/search?l=PHP&p=" + str(p) + "&q=followers%3A%3E%3D1000+filename%3ACodeIgniter.php+followers%3A%3E1000+language%3APHP+language%3APHP&ref=advsearch&type=Users"
                browser.get(url)
            time.sleep(5)
            links = browser.find_elements_by_tag_name("a")
            try:
                for link in links:
                    if link.is_displayed() and link.is_enabled():
                        try:
                            classname = link.get_attribute('class')
                            if classname == "mr-1":
                                #print(link.get_attribute('href'))
                                user_lists.append(link.get_attribute('href').strip())
                                
                        except:
                            pass
            except:
                pass
            
        return user_lists
    except Exception as e:
        raise e
    
def GetTotalPages():
    try:
        global browser
        print("[+] collect pages")
        maxpage = 1
        links = browser.find_elements_by_tag_name("a")
        try:
            for link in links:
                try:
                    attr = link.get_attribute('aria-label')
                    if attr.find("Page ") != -1:
                        maxpage = int(attr.replace("Page ", ""))
                except:
                    pass
        except:
            pass
        
        return maxpage
    except Exception as e:
        raise e
   
def split(a, n):
    try:
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    except:
        pass

def ExamineLists(dat):
    try:
        global global_ci_user_lists
        for url in dat:
            url = url + "?tab=repositories&q=" + config.keyword
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
            try:
                response = requests.get(url.strip(), headers=headers, timeout=9)
                if response.text.find("have any repositories that match") == -1:
                    print("[+] got user : " + url)
                    global_ci_user_lists.append(url)
                else:
                    #profile check
                    soup = BeautifulSoup(response.text, "lxml")
                    res = soup.select_one('.user-profile-bio')
                    data = res.text.lower()
                    if (data.find(config.keyword) != -1):
                        print("[+] got user from profile : " + url)
                        global_ci_user_lists.append(url)
                    #eof profile check
            except Exception as e:
                print("-")
                raise e
            
    except Exception as e:
        raise e
    
def RunThread(user_lists):
    try:
        global thread_number
        t = [None] * 100
        print("[+] run thread")
        jum = len(user_lists)
        datas = split(user_lists, thread_number)
        i = 0 
        for dat in datas:
            t[i] = threading.Thread(target=ExamineLists, args=(dat,))
            t[i].start()
            t[i].join()
            i = i + 1
    except Exception as e:
        raise e
    
def CollectData(user_url):
    try:
        url = user_url.replace("?tab=repositories&q=" + config.keyword, "")
        print(url)
        dataku = "\n===================================\n"
        dataku += "github : " + url + "\n"
        user = url.replace("https://github.com/", "")
        dataku += "user : " + user + "\n"
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        try:
            response = requests.get(url.strip(), headers=headers, timeout=9)
            data = response.text
            soup = BeautifulSoup(data, "lxml")
            
            for li in soup.findAll('li', {"class": "vcard-detail"}):
                dataku += li.text.replace("\n\n", "\n")
            
            name = soup.find('span', {"class": "vcard-fullname"})
            nama = name.text.replace("\n", "").strip()
            dataku += "name : " + nama + "\n"
        except:
            pass
        with open("log.txt", "a") as file_object:
            file_object.write(dataku)
            
        MoreProfiling(user, nama)
            
    except Exception as e:
        raise e
   
def MoreProfiling(user, nama):
    try:
        global browser
        dataku = ""
        block = ["bing", "microsoft", "wikipedia", "webster"]
        konten = ["twitter", "instagram", "linkedin", "email", "@", "facebook"]
        print("[+] more profiling for " + user)
        url = "https://www.bing.com/search?q=" + user
        browser.get(url)
        WaitForFingerprint("2022 Microsoft")
        time.sleep(1)
        lnks = browser.find_elements_by_tag_name("a")
        for lnk in lnks:
            try:
                url = lnk.get_attribute("hover-url")
                if url is not None:
                    try:
                        eksis = 0
                        for bl in block:
                            if url.find(bl) != -1:
                                eksis = 1
                                break
                        if eksis == 0:
                            for k in konten:
                                if url.find(k) != -1:
                                    print(url)
                                    dataku += url + "\n"
                                    break
                    except:
                        pass
            except:
                raise
        
        cites = browser.find_elements_by_tag_name("cite")
        for cite in cites:
            try:
                cteks = cite.text
                if cteks is not None:
                    try:
                        eksis = 0
                        for bl in block:
                            if cteks.find(bl) != -1:
                                eksis = 1
                                break
                        if eksis == 0:
                            for k in konten:
                                if k.find(k) != -1:
                                    print(cteks)
                                    dataku += url + "\n"
                                    break
   
                    except:
                        pass
                    

            except:
                raise
        
        
        with open("log.txt", "a") as file_object:
            file_object.write(dataku)
            
        
    except Exception as e:
        raise e
    
def Main():
    try:
        global page_switch, thread_number, global_ci_user_lists
        
        list_userci3 = []
        count = 0
        InitDir()
        Init()
        WaitForFingerprint("2022 GitHub, Inc")
        InjectJsFile("jquery.min.js")
        maxpage = int(GetTotalPages())
        print("[+] max page : " + str(maxpage))
        #user_lists = ["https://github.com/hex-ci","https://github.com/ehoneahobed", "https://github.com/ad4mny", "https://github.com/tomnomnom"]
        user_lists = CollectUsers(maxpage)
        RunThread(user_lists)
        for user in global_ci_user_lists:
            CollectData(user)
            
            
    except Exception as e:
        raise e
        #pass
    
if __name__ == "__main__":
    Main()
