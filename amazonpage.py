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
import baseaction
from locator import AmazonPageLocator


class AmazonPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonPageLocator

    def enter_amazon_page(self):
        return

    def check_page_loaded(self, *locator):
        return False

    def goto_top(self):
        return False

    def enter_account_page(self):
        return False

    def enter_wishlist(self):
        return False

    def enter_cart(self):
        return False

    def enter_orders(self):
        return False

    def random_walk(self):
        return

    def is_search_box_displayed(self):
        return

    def enter_sign_in_page(self):
        return

    def search_asin(self):
        return