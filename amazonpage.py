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
from locator import AmazonPageLocator
from amazonsigninpage import AmazonSignInPage


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
        return self.driver.find_element(*locator)

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

    def enter_sign_in_page(self):
        self.hover(self.locator.ACCOUNT)
        self.random_sleep(1, 3)
        self.click(self.locator.SIGNIN)
        return AmazonSignInPage(self.driver)

    def search_asin(self, keyword):
        try:
            time.sleep(random.randint(3, 6))
            # browser.execute_script('window.stop()')
            input_box = driver.find_element_by_id('twotabsearchtextbox')
        except Exception as e:
            print(type(e))
            print("找不到输入框")
        else:
            if input_box.is_displayed():
                print("找到输入框")
                driver.set_page_load_timeout(1)
                driver.set_script_timeout(1)
                for character in keyword:
                    try:
                        input_box.send_keys(character)
                        time.sleep(random.randint(300, 800) / 1000)  # pause for 0.3 seconds
                    except Exception as e:
                        print(type(e))
                        try:
                            input_box.send_keys(character)
                            time.sleep(random.randint(300, 800) / 1000)  # pause for 0.3 seconds
                        except Exception as e:
                            print(type(e))
                            pass
                        finally:
                            pass
                driver.set_page_load_timeout(15)
                driver.set_script_timeout(15)

if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
    driver = webdriver.Chrome(chrome_options=option)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)
    page = AmazonPage(driver)
    page.enter_us_amazon_page()
    time.sleep(5)
    driver.quit()