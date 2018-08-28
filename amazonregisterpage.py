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
from locator import AmazonRegisterPageLocator


class AmazonRegisterPage(AmazonPage):
    def __init__(self, driver):
        self.drvier = driver
        self.locator = AmazonRegisterPageLocator

    def fill_in_form(self, *info):
        return
