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
from locator import AmazonAsinPageLocator
from selenium.common.exceptions import NoSuchElementException



class AmazonAsinPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonAsinPageLocator

    def add_cart(self, begin, end):
        self.click(*self.locator.ADDCARTBUTTON)
        self.random_sleep(begin, end)
        print("加入购物车。。。\n")

    def ask_qa(self, content, begin, end):
        self.click(*self.locator.QATEXT)
        self.random_sleep(1000, 2000)
        self.input(content, *self.locator.QATEXT)
        self.random_sleep(3000, 6000)
        self.click(*self.locator.QAENTRYBUTTON)
        self.random_sleep(2000, 3000)
        # if self.is_element_exsist(*self.locator.QAPOSTBUTTON):
        #     print("QA post button is ready!\n")
        self.click(*self.locator.QAPOSTBUTTON)
        self.random_sleep(begin, end)
        print("提交QA： " + content + "\n")

    def add_wishlist(self, begin, end):
        country = self.cf.get("account", "country")
        self.click(*self.locator.ADDWISHLISTSUBMITBUTTON)
        self.random_sleep(1000, 2000)
        if self.is_element_exsist(*self.locator.CREATELISTBUTTON):
            if country == "us":
                self.click(*self.locator.WISHLISTSELETE)
                self.random_sleep(1000, 2000)
            self.click(*self.locator.CREATELISTBUTTON)

        print("添加心愿卡。。。。\n")
        self.random_sleep(begin, end)

