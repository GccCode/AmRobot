#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import json
import os
import win32api
import win32con
import pyautogui
from win32api import GetSystemMetrics
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from baseaction import BaseAction
from amazonpage import AmazonPage
from locator import AmazonRegisterPageLocator


class AmazonRegisterPage(AmazonPage):
    def __init__(self, driver):
        self.drvier = driver
        self.locator = AmazonRegisterPageLocator

    def fill_in_form(self, *info):
        self.input("username", *self.locator.USERENAME)
        time.sleep(random.randint(2,5))
        self.input("username@yahoo.com", *self.locator.EMAILNAME)
        time.sleep(random.randint(2, 5))
        self.input("123456789", *self.locator.PASSWORD)
        time.sleep(random.randint(2, 5))
        self.input("123456780", *self.locator.PASSWORDCHECK)
        time.sleep(random.randint(2, 5))
        self.click(*self.locator.CONTINUESUBMIT)

if __name__ == "__main__":
    #option = webdriver.ChromeOptions()
    #option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
    #driver = webdriver.Chrome(chrome_options=option)
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    page = AmazonPage(driver)
    page.enter_us_amazon_page()
    time.sleep(5)
    page.search_asin("echo dot")
    time.sleep(5)
    page.enter_register_page()
    time.sleep(5)
    registerpage = AmazonRegisterPage(driver)
    registerpage.fill_in_form()
    time.sleep(5)
    driver.quit()
