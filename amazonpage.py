#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import random
from selenium import webdriver
from baseaction import BaseAction
from locator import AmazonPageLocator


class AmazonPage(BaseAction):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonPageLocator

    def enter_us_amazon_page(self):
        self.driver.get('https://www.amazon.com')
        self.wait_page_loaded(*self.locator.LOGO)

    def enter_jp_amazon_page(self):
        self.driver.get('https://www.amazon.co.jp')
        self.wait_page_loaded(*self.locator.LOGO)

    def wait_page_loaded(self, *locator):
        self.driver.find_element(*locator)

    def goto_top(self):
        self.scoll_to_top()
        self.wait_page_loaded(*self.locator.LOGO)

    def enter_account_page(self):
        return False

    def enter_wishlist(self):
        return False

    def enter_cart(self):
        return False

    def enter_orders(self):
        return False

    def enter_prime(self):
        return

    def random_walk(self):
        return

    def is_search_box_displayed(self):
        return

    def enter_register_page(self):
        result = random.randint(1,2)
        self.hover(*self.locator.ACCOUNT)
        self.random_sleep(1, 3)
        if result == 1:
            self.click(*self.locator.SIGNIN)
            self.random_sleep(1, 3)
            self.click(*self.locator.CREATEACCOUNTSUBMIT)
        else:
            self.click(*self.locator.STARTHERE)

    def search_asin(self, keyword):
        self.input("echo dot mount", *self.locator.SEARCH)
        self.click(*self.locator.SUBMITKEYWORD)

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
    driver.quit()