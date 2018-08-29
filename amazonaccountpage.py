#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
from amazonpage import AmazonPage
from locator import AmazonAccountPageLocator


class AmazonAccountPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonAccountPageLocator

    def enter_address_page(self):
        self.click(*self.locator.YOURADDRESS_US)
        self.random_sleep(3000, 5000)
        self.wait_page_loaded(*self.locator.ADDADDRESS)

    def enter_payment_page(self):
        cf = configparser.ConfigParser()
        cf.read("info.txt")
        country = cf.get("account", "country")
        if country == "us":
            self.click(*self.locator.PAYMENTOPTIONS_US)
        elif country == "jp":
            self.click(*self.locator.PAYMENTOPTIONS_JP)
        self.random_sleep(3000, 5000)
        self.wait_page_loaded(*self.locator.WALLETTITLE)