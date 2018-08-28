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
    PRIME = (By.ID, "nav-link-prime")
    CART = (By.ID, "nav-cart")
    ORDERS = (By.ID, "nav-orders")
    WISHLIST = (By.XPATH, '//*[@id=\'nav-flyout-wl-items\']/div/a[position()=1]/span')

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
    USERENAME = (By.ID, 'ap_customer_name')
    PRONUNCIATION = (By.ID, 'ap_customer_name_pronunciation')
    EMAILNAME = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    PASSWORDCHECK = (By.ID, 'ap_password_check')
    CONTINUESUBMIT = (By.ID, 'continue')