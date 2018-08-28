#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import random
from selenium import webdriver
from amazonpage import AmazonPage
from locator import AmazonRegisterPageLocator
import configparser


class AmazonRegisterPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonRegisterPageLocator

    def fill_in_form(self, *info):
        cf = configparser.ConfigParser()
        cf.read("account.txt")
        username = cf.get("account", "username")
        country = cf.get("account", "country")
        emailname = cf.get("account", "email")
        password = cf.get("account", "password")
        self.input(username, *self.locator.USERENAME)
        time.sleep(random.randint(2,5))
        if country == 'jp':
            pronunciation = cf.get("account", "pronunciation")
            self.input(pronunciation, *self.locator.PRONUNCIATION)
        self.input(emailname, *self.locator.EMAILNAME)
        time.sleep(random.randint(2, 5))
        self.input(password, *self.locator.PASSWORD)
        time.sleep(random.randint(2, 5))
        self.input(password, *self.locator.PASSWORDCHECK)
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
    page.enter_amazon_page()
    time.sleep(5)
    page.search_asin("echo dot")
    time.sleep(5)
    page.enter_register_page()
    time.sleep(5)
    registerpage = AmazonRegisterPage(driver)
    registerpage.fill_in_form()
    time.sleep(5)
    driver.quit()
