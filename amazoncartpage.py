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
from locator import AmazonCartPageLocator


class AmazonCartPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonCartPageLocator

    def delete_asin(self, asin):
        return

    def clear_cart(self, *asin):
        return

    def checkout(self):
        return