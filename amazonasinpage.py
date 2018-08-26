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

    def view_image(self):
        return

    def random_view(self):
        return

    def find_sponosored_asins(self):
        return

    def enter_sponsored_asins(self):
        return

    def enter_sellers(self):
        return

    def add_cart(self):
        return

    def proceed_to_checkout(self):
        return

    def enter_current_cart(self):
        return

    def add_wishlist(self):
        return
