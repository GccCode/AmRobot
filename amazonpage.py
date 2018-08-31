#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import random
from selenium import webdriver
from baseaction import BaseAction
from locator import AmazonPageLocator
from win32api import GetSystemMetrics
import configparser
from selenium.common.exceptions import NoSuchElementException


class AmazonPage(BaseAction):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonPageLocator
        self.cf = configparser.ConfigParser()
        self.cf.read("info.txt")
        self.cf_kw = configparser.ConfigParser()
        self.cf_kw.read("keywords.txt")
        self.screen_width = GetSystemMetrics(0)
        self.screen_heigth = GetSystemMetrics(1)

    def enter_amazon_page(self, begin, end):
        country = self.cf.get("account", "country")
        if country == 'us':
            self.driver.get('https://www.amazon.com')
        elif country == 'jp':
            self.driver.get('https://www.amazon.co.jp')
        self.random_sleep(begin, end)
        self.wait_page_loaded(*self.locator.LOGO)

    def wait_page_loaded(self, *locator):
        self.driver.find_element(*locator)

    def goto_top(self, begin, end):
        self.scoll_to_top()
        self.wait_page_loaded(*self.locator.LOGO)
        self.random_sleep(begin, end)

    def enter_account_page(self, begin, end):
        self.click(*self.locator.ACCOUNT)
        self.random_sleep(begin, end)

    def enter_wishlist(self):
        self.hover(*self.locator.ACCOUNT)
        self.random_sleep(random.randint(1000, 2000) / 1000)
        self.click(*self.locator.WISHLIST)

    def enter_cart(self):
        self.click(*self.locator.CART)

    def enter_orders(self):
        self.click(*self.locator.ORDERS)

    def enter_prime(self, begin, end):
        self.click(*self.locator.PRIME)
        self.random_sleep(1000, 2000)
        self.click(*self.locator.PRIMEFREETRIAL)
        self.random_sleep(1000, 2000)
        self.click(*self.locator.PRIMESTARTTRIAL)
        self.random_sleep(begin, end)

    def random_walk(self, count):
        i = 0
        while i < count:
            self.random_mouse_move()
            self.random_mouse_scoll()
            i += 1

    def enter_signin_page(self, begin, end):
        self.hover(*self.locator.ACCOUNT)
        self.random_sleep(1000, 2000)

        try:
            self.click(*self.locator.SIGNOUT)
        except NoSuchElementException as msg:
            self.click(*self.locator.SIGNIN)

        self.random_sleep(begin, end)

    def enter_register_page(self, begin, end):
        result = random.randint(1,2)
        if result == 1:
            self.hover(*self.locator.ACCOUNT)
            self.random_sleep(1000, 2000)
            result = random.randint(1, 2)
            if result == 1:
                self.click(*self.locator.SIGNIN)
                self.random_sleep(1000, 2000)
                self.click(*self.locator.CREATEACCOUNTSUBMIT)
            else:
                self.click(*self.locator.STARTHERE)
        else:
            self.click(*self.locator.ACCOUNT)
            self.random_sleep(1000, 2000)
            self.click(*self.locator.CREATEACCOUNTSUBMIT)

        self.random_sleep(begin, end)

    def search_asin(self, keyword, begin, end):
        self.input(keyword, *self.locator.SEARCH)
        self.click(*self.locator.SUBMITKEYWORD)

# if __name__ == "__main__":
#     #option = webdriver.ChromeOptions()
#     #option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
#     #driver = webdriver.Chrome(chrome_options=option)
#     driver = webdriver.Chrome()
#     driver.set_page_load_timeout(30)
#     driver.set_script_timeout(30)
#     page = AmazonPage(driver)
#     page.enter_amazon_page()
#     time.sleep(5)
#     page.search_asin("echo dot")
#     time.sleep(5)
#     page.enter_register_page()
#     driver.quit()