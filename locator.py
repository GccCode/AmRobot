#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By


class AmazonPageLocator(object):
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNIN = (By.XPATH, '//*[@id=\'nav-flyout-ya-signin\']/a[position()=1]')
    STARTHERE = (By.XPATH, '//*[@id=\'nav-flyout-ya-newCust\']/a')
    CREATEACCOUNTSUBMIT = (By.ID, 'createAccountSubmit')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SUBMITKEYWORD = (By.XPATH, '//*[@id=\'nav-search\']/form/div[position()=2]/div/input')

class AmazonAccountPageLocator(AmazonPageLocator):
    LOGO = 0

class AmazonAsinPageLocator(AmazonPageLocator):
    LOGO = 0

class AmazonCartPageLocator(AmazonPageLocator):
    LOGO = 0

class AmazonPaymentLocator(AmazonPageLocator):
    LOGO = 0

class AmazonSearchPageLocator(AmazonPageLocator):
    LOGO = 0

class AmazonRegisterPageLocator(AmazonPageLocator):
    LOGO = 0