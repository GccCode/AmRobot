#!/usr/bin/env python
# -*- coding:utf-8 -*-


from amazonpage import AmazonPage
from locator import AmazonSearchPageLocator
import configparser
from selenium.common.exceptions import NoSuchElementException
import random


class AmazonSearchPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonSearchPageLocator
        self.cf_kw = configparser.ConfigParser()
        self.cf_kw.read("keywords.txt")

    def find_target_asin(self, asin):
        asinresults = self.driver.find_elements(*self.locator.ASINRESULTS)
        for asinresult in asinresults:
            if asinresult.get_attribute('data-asin') == asin:
                return asinresult
        return False

    def is_asin_amazon_choice(self, asinresult, asin):
        status = True
        try:
            asinresult.find_element_by_id("AMAZONS_CHOICE_"+ asin + "-supplementary")
        except NoSuchElementException as msg:
            status = False
        finally:
            return status

    def is_asin_sponsored(self, asinresult, asin):
        status =True
        try:
            asinresult.find_element_by_id("a-popover-sponsored-header-" + asin)
        except NoSuchElementException as msg:
            status = False
        finally:
            return status

    def click_asin_by_img(self, asinresult, asin):
        if self.is_asin_amazon_choice(asinresult, asin):
            asinresult.find_element(*self.locator.ASINIMAGE_AC).click()
        else:
            asinresult.find_element(*self.locator.ASINIMAGE).click()

    def click_asin_by_title(self, asinresult, asin):
        if self.is_asin_amazon_choice(asinresult, asin):
            asinresult.find_element(*self.locator.ASINTITLE_AC).click()
        else:
            asinresult.find_element(*self.locator.ASINTITLE).click()

    def enter_asin_page(self, asinresult, asin, begin, end):
        option = random.randint(1, 2)
        if option == 1:
            self.click_asin_by_img(asinresult, asin)
        else:
            self.click_asin_by_title(asinresult, asin)

        self.random_sleep(begin, end)

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