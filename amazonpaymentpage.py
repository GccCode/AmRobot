#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from amazonpage import AmazonPage
from locator import AmazonPaymentPageLocator
from amazonaccountpage import AmazonAccountPage
import configparser


class AmazonPaymentPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonPaymentPageLocator

    def add_new_payment(self):
        cf = configparser.ConfigParser()
        cf.read("info.txt")
        fullname = cf.get("bill_address", "username")
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


if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
    driver = webdriver.Chrome(chrome_options=option)
    #driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    page = AmazonPage(driver)
    page.enter_amazon_page()
    page.random_sleep(3000, 5000)
    page.enter_account_page()
    page.random_sleep(3000, 5000)
    accountpage = AmazonAccountPage(driver)
    accountpage.enter_payment_page()
    page.random_sleep(3000, 5000)
    paymentpage = AmazonPaymentPage(driver)
    paymentpage.add_new_payment()
    page.random_sleep(3000, 5000)
    driver.quit()