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
from locator import AmazonSearchPage


class AmazonSearchPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonSearchPage

    def find_target_asin(self, asin):
        return

    def enter_target_asin(self, asin):
        return

    def find_prev_asin(self, asin):
        return

    def enter_prev_asin(self, asin):
        return

    def find_next_asin(self, asin):
        return

    def enter_next_asin(self, asin):
        return

    def find_asin_ads(self, asin):
        return

    def enter_asin_ads(self, asin):
        return

    def save_page(self, asin):
        return

    def restore_page(self, asin):
        return

    def next_page(self, asin):
        return