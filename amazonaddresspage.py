#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from amazonpage import AmazonPage
from amazonaccountpage import AmazonAccountPage
from locator import AmazonAddressPageLocator
import configparser

class AmazonAddressPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonAddressPageLocator

    def add_address(self, addresstype):
        self.click(*self.locator.ADDADDRESS)
        self.random_sleep(1000, 2000)
        self.fill_in_form(addresstype)

    def fill_in_form(self, addresstype):
        cf = configparser.ConfigParser()
        cf.read("info.txt")
        country = cf.get("account", "country")
        if addresstype == "bill":
            fullname = cf.get("bill_address", "fullname")
            line1 = cf.get("bill_address", "addressline1")
            line2 = cf.get("bill_address", "addressline2")
            phonenumber = cf.get("bill_address", "phone")
            if country == "us":
                city = cf.get("bill_address", "city")
                state = cf.get("bill_address", "state")
                postalcode = cf.get("bill_address", "postalcode")
        elif addresstype == "fba":
            fullname = cf.get("fba_address", "fullname")
            line1 = cf.get("fba_address", "addressline1")
            line2 = cf.get("fba_address", "addressline2")
            phonenumber = cf.get("fba_address", "phone")
            if country == "us":
                city = cf.get("fba_address", "city")
                state = cf.get("fba_address", "state")
                postalcode = cf.get("fba_address", "postalcode")

        self.click(*self.locator.FULLNAME)
        self.random_sleep(1000, 2000)
        self.input(fullname, *self.locator.FULLNAME)
        self.random_sleep(1000, 2000)

        self.click(*self.locator.ADDRESSLINE1)
        self.random_sleep(1000, 2000)
        self.input(line1, *self.locator.ADDRESSLINE1)
        self.random_sleep(1000, 2000)

        if country == "jp":
            self.click(*self.locator.ADDRESSLINE2)
            self.random_sleep(1000, 2000)
            self.input(line2, *self.locator.ADDRESSLINE2)
            self.random_sleep(1000, 2000)

        if country == "us":
            self.click(*self.locator.ADDRESSCITY)
            self.random_sleep(1000, 2000)
            self.input(city, *self.locator.ADDRESSCITY)
            self.random_sleep(1000, 2000)

            self.click(*self.locator.ADDRESSSTATE)
            self.random_sleep(1000, 2000)
            self.input(state, *self.locator.ADDRESSSTATE)
            self.random_sleep(1000, 2000)

            self.click(*self.locator.ADDRESSPOSTALCODE)
            self.random_sleep(1000, 2000)
            self.input(postalcode, *self.locator.ADDRESSPOSTALCODE)
            self.random_sleep(1000, 2000)
        elif country == "jp":
            self.click(*self.locator.ADDRESSSTATE)
            self.random_sleep(1000, 2000)
            self.input(state, *self.locator.ADDRESSSTATE)
            self.random_sleep(1000, 2000)

            self.click(*self.locator.ADDRESSPOSTALCODE)
            self.random_sleep(1000, 2000)
            self.input(postalcode, *self.locator.ADDRESSPOSTALCODE)
            self.random_sleep(1000, 2000)

        self.click(*self.locator.ADDRESSPHONE)
        self.random_sleep(1000, 2000)
        self.input(phonenumber, *self.locator.ADDRESSPHONE)
        self.random_sleep(1000, 2000)

        self.click(*self.locator.ADDADDRESSSUBMIT)
        self.wait_page_loaded(*self.locator.ADDADDRESS)


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
    accountpage.enter_address_page()
    page.random_sleep(3000, 5000)
    addresspage = AmazonAddressPage(driver)
    addresspage.add_address("bill")
    page.random_sleep(3000, 5000)

    page.enter_account_page()
    page.random_sleep(3000, 5000)
    accountpage.enter_address_page()
    page.random_sleep(3000, 5000)
    addresspage.add_address("fba")
    page.random_sleep(3000, 5000)
    driver.quit()