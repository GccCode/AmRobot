#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from amazonpage import AmazonPage
from locator import AmazonSignInPageLocator
import configparser
from selenium.common.exceptions import NoSuchElementException


class AmazonSignInPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonSignInPageLocator
        self.cf = configparser.ConfigParser()
        self.cf.read("info.txt")

    def sign_in(self, begin, end):
        self.fill_in_form()
        self.random_sleep(begin, end)

    def fill_in_form(self):
        emailname = self.cf.get("account", "email")
        password = self.cf.get("account", "password")
        try:
            self.click(*self.locator.ACCOUNTSWITCHER)
            self.random_sleep(1000, 2000)
        except NoSuchElementException as msg:
            self.click(*self.locator.EMAILNAME)
            self.random_sleep(1000, 2000)
            self.input(emailname, *self.locator.EMAILNAME)
            self.random_sleep(1000, 2000)
            self.click(*self.locator.CONTINUE)
            self.random_sleep(1000, 2000)
            self.click(*self.locator.PASSWORD)
            self.random_sleep(1000, 2000)
            self.input(password, *self.locator.PASSWORD)
            self.random_sleep(1000, 2000)
            self.click(*self.locator.SIGNINSUBMIT)
        else:
            self.click(*self.locator.PASSWORD)
            self.random_sleep(1000, 2000)
            self.input(password, *self.locator.PASSWORD)
            self.random_sleep(1000, 2000)
            self.click(*self.locator.SIGNINSUBMIT)
