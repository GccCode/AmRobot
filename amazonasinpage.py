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



class AmazonAsinPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonAsinPageLocator

    def view_random_image(self, begin, end):
        imageresults = self.driver.find_element(*self.locator.IMAGES).find_elements(".//[contains(@id, \'a-autoid-\')]")
        count = random.randint(1, len(imageresults))
        for i in range(1, count):
            index = random.randint(1, len(imageresults))
            imageresults[index].click()
            self.random_sleep(1000, 2000)
            self.hover(*self.locator.LOADINGIMAGE)
            self.random_sleep(begin, end)
        print("随机浏览产品图片，数量：" + str(count), + "\n")

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
        if self.is_element_exsist(*self.locator.QAPOSTBUTTON):
            print("QA post button is ready!\n")
        # self.click(*self.locator.QAPOSTBUTTON)
        self.random_sleep(begin, end)
        print("提交QA： " + content + "\n")

    def add_wishlist(self, type, begin, end):
        self.click(*self.locator.ADDWISHLISTSUBMITBUTTON)
        if self.is_element_exsist(*self.locator.CREATELISTBUTTON):
            self.click(*self.locator.WISHLISTSELETE)
            self.random_sleep(1000, 2000)
            # self.click(*self.locator.CREATELISTBUTTON)

        print("添加心愿卡。。。。\n")
        self.random_sleep(begin, end)

