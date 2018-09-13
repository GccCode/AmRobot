#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import string
import time
import requests
import sys
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import re
import configparser
from selenium import webdriver
from amazonpage import AmazonPage
from amazonregisterpage import AmazonRegisterPage
from amazonaccountpage import AmazonAccountPage
from amazonaddresspage import AmazonAddressPage
from amazonpaymentpage import AmazonPaymentPage
from amazonsigninpage import AmazonSignInPage
from amazonsearchpage import  AmazonSearchPage
from amazonasinpage import  AmazonAsinPage
import os, win32gui, win32ui, win32con, win32api
import io
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

#0)
#1) Chrome
#2) Firefox+Win7:
#3) Safari+Win7:
#4) Opera+Win7:
#5) IE+Win7+ie9：
#6) Win7+ie8：
#7) WinXP+ie8：
#8) WinXP+ie7：
#9) WinXP+ie6：
useragentlist = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
]

def customized_broswer():
    option = webdriver.ChromeOptions()
    # index = random.randint(0, (len(useragentlist) - 1))
    # useragent = "--user-agent=" + useragentlist[index]
    # option.add_argument(useragent)
    driver =  webdriver.Chrome(chrome_options=option)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    driver.maximize_window()
    return driver

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # cf = configparser.ConfigParser()
    # cf.read("task.txt")

    driver = customized_broswer()
    t1 = time.time()
    try:
        amazonpage = AmazonPage(driver)
        driver.get('https://www.amazon.com')
        time.sleep(random.randint(3, 5))
        searchpage = AmazonSearchPage(driver)
        asinresult = False
        entry_type = "sponsored"
        keyword = "swing swivel"
        #asin = "B01HWSQIGM"
        asin = "B075C6G6M1"
        print(("* 开始搜索关键词。。。"), flush=True)
        amazonpage.search_asin(keyword, 8000, 10000)
        asinresult = searchpage.find_target_product_rank(asin, entry_type, int(5))
        if asinresult != False:
            pass
        else:
            print(("找不到产品！！！！"), flush=True)
    except NoSuchElementException as msg:
        print(("* 找不到元素。。。"), flush=True)
    except TimeoutException as msg:
        print(("* 网页加载超时。。。"), flush=True)
    except:
        pass
    finally:
        t2 = time.time()
        print("总耗时：" + format(t2 - t1))
        input("xxxxxx")
        driver.quit()
