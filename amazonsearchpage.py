#!/usr/bin/env python
# -*- coding:utf-8 -*-


from amazonpage import AmazonPage
from locator import AmazonSearchPageLocator
import configparser
from win32api import GetSystemMetrics
from selenium.common.exceptions import NoSuchElementException
import random


class AmazonSearchPage(AmazonPage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AmazonSearchPageLocator
        self.cf = configparser.ConfigParser()
        self.cf.read("info.txt")
        self.cf_kw = configparser.ConfigParser()
        self.cf_kw.read("keywords.txt")
        self.screen_width = GetSystemMetrics(0)
        self.screen_heigth = GetSystemMetrics(1)

    def find_target_product(self, asin, type):
        for page in range(1, 5):
            asinresult = self.find_target_asin(asin, type)
            if asinresult != False:
                print("page - " + str(page) + "\n")
                return asinresult
            else:
                self.random_walk(random.randint(1, 3))
                self.enter_next_page(3000, 5000)
        return False

    def enter_random_products(self, count, begin, end):
        self.log_location()
        for i in range(1, count):
            self.enter_random_product(False, begin, end)

    def enter_random_product(self, asin, begin, end):
        self.log_location()
        index = 0
        asinresults = self.driver.find_elements(*self.locator.ASINRESULTS)
        if asin == False:
            tmp = random.randint(0, (len(asinresults) - 1))
            currenthandle = self.enter_asin_page(asinresults[tmp], asinresults[tmp].get_attribute('data-asin'), 3000, 10000)
            self.back_prev_page(currenthandle, begin, end)
        else:
            for asinresult in asinresults:
                if asinresult.get_attribute('data-asin') == asin:
                    tmp = random.randint(0, (len(asinresults) - 1))
                    print("tmp = " + str(tmp) + "\n")
                    print("index = " + str(index) + "\n")
                    while tmp == index:
                        tmp = random.randint(0, (len(asinresults) - 1))

                    currenthandle = self.enter_asin_page(asinresults[tmp], asinresults[tmp].get_attribute('data-asin'), 3000, 8000)
                    self.back_prev_page(currenthandle, begin, end)
                    break
                else:
                    index += 1

    def find_target_asin(self, asin, type):
        self.log_location()
        asinresults = self.driver.find_elements(*self.locator.ASINRESULTS)
        for asinresult in asinresults:
            if asinresult.get_attribute('data-asin') == asin:
                if type == "normal":
                    if self.is_asin_sponsored(asinresult, asin) != True:
                        return asinresult
                elif type == "sponsored":
                    if self.is_asin_sponsored(asinresult, asin):
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

    def is_asin_bestseller(self, asinresult, asin):
        status = True
        try:
            asinresult.find_element_by_id("BESTSELLER_" + asin + "-supplementary")
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

    def click_asin_by_img_jp(self, asinresult, asin):
        asinresult.find_element(*self.locator.ASINIMAGE_JP).click()

    def click_asin_by_title_jp(self, asinresult, asin):
        if self.is_asin_sponsored(asinresult, asin):
            asinresult.find_element(*self.locator.ASINTITLE_SP_JP).click()
        else:
            asinresult.find_element(*self.locator.ASINTITLE_JP).click()

    def click_asin_by_img(self, asinresult, asin):
        if self.is_asin_amazon_choice(asinresult, asin):
            asinresult.find_element(*self.locator.ASINIMAGE_AC).click()
        elif self.is_asin_bestseller(asinresult, asin):
            asinresult.find_element(*self.locator.ASINIMAGE_BS).click()
        else:
            asinresult.find_element(*self.locator.ASINIMAGE).click()

    def click_asin_by_title(self, asinresult, asin):
        if self.is_asin_amazon_choice(asinresult, asin):
            asinresult.find_element(*self.locator.ASINTITLE_AC).click()
        elif self.is_asin_sponsored(asinresult, asin):
            asinresult.find_element(*self.locator.ASINTITLE_SP).click()
        elif self.is_asin_bestseller(asinresult, asin):
            asinresult.find_element(*self.locator.ASINTITLE_BS).click()
        else:
            asinresult.find_element(*self.locator.ASINTITLE).click()

    def enter_asin_page(self, asinresult, asin, begin, end):
        self.log_location()
        country = self.cf.get("account", "country")
        option = random.randint(1, 2)
        if option == 1:
            print("enter by image link..\n")
            if country == 'us':
                self.click_asin_by_img(asinresult, asin)
            elif country == "jp":
                self.click_asin_by_img_jp(asinresult, asin)
        else:
            print("enter by title link..\n")
            if country == 'us':
                self.click_asin_by_title(asinresult, asin)
            elif country == "jp":
                self.click_asin_by_title_jp(asinresult, asin)

        self.random_sleep(begin, end)
        return self.driver.current_window_handle

    def find_asin_ads(self, asin):
        return

    def enter_asin_ads(self, asin):
        return

    def close_page(self):
        self.driver.close()

    def switch_to_new_page(self, currenthandle):
        handles = self.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口（切换到搜狗）
            if handle != currenthandle:
                self.driver.switch_to_window(handle)
                break

    def back_prev_page(self, handle, begin, end):
        country = self.cf.get("account", "country")
        if country == "jp":
            self.switch_to_new_page(handle)
            self.close_page()
            self.driver.switch_to_window(handle)
            self.random_sleep(begin, end)
        elif country == "us":
            self.switch_to_new_page(handle)
            self.navigation_back(begin, end)
            self.driver.switch_to_window(handle)

    def enter_next_page(self, begin, end):
        self.log_location()
        self.click(*self.locator.PAGENEXTSTRING)
        self.random_sleep(begin, end)