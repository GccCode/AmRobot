#!/usr/bin/env python
# -*- coding:utf-8 -*-

from amazonpage import AmazonPage
from locator import AmazonPaymentPageLocator
import configparser


class AmazonPaymentPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonPaymentPageLocator

    def add_new_payment(self):
        cf = configparser.ConfigParser()
        cf.read("info.txt")
        fullname = cf.get("address", "fullname")
        cardnum = cf.get("cardinfo", "cardnumer")
        validmonth = cf.get("cardinfo", "month")
        validyear = cf.get("cardinfo", "year")

        self.click(*self.locator.CARDHOLDER_US)
        self.random_sleep(1000, 2000)
        self.input(fullname, *self.locator.CARDHOLDER_US)
        self.random_sleep(1000, 2000)

        self.click(*self.locator.CARDNUMBER_US)
        self.random_sleep(1000, 2000)
        self.input(cardnum, *self.locator.CARDNUMBER_US)
        self.random_sleep(1000, 2000)

        self.select((int(validmonth) - 1), *self.locator.VALIDMON_US)
        self.random_sleep(1000, 2000)
        self.select((int(validyear) - 2018), *self.locator.VALIDYEAR_US)
        self.random_sleep(1000, 2000)

        self.click(*self.locator.ADDCARD)
        self.random_sleep(2000, 4000)
        self.wait_page_loaded(*self.locator.PAYMENTADDED)