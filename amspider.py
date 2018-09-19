#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import re
import sys
import io
from selenium.webdriver.common.by import By
from amazonasinpage import AmazonAsinPage
from selenium.common.exceptions import NoSuchElementException


item_prefix = "//*[@id=\'zg-ordered-list\']/li[position()="
item_postfix = "]/span"
price_symbol = ".//div/span/div[position()=2]/a[position()=1]/span/span"
review_symbol = ".//div/span/div[position()=1]/a[position()=2]"
href_symbol = ".//div/span/div[position()=2]/a[position()=1]"
rate_symbol = ".//div/span/div[position()=1]/a"
BUYER_COUNT = (By.XPATH, '//*[@id=\'olp_feature_div\']/div/span[position()=1]/a')
QA_COUNT = (By.XPATH, '//*[@id=\'askATFLink\']/span')
FBA_FLAG = (By.ID, "SSOFpopoverLink")
NO_THANKS = (By.ID, 'attachSiNoCoverage')
VIEW_CART_BUTTON = (By.ID, 'attach-sidesheet-view-cart-button')
VIEW_CART_BUTTON1 = (By.ID, 'hlb-view-cart')
PRODUCT_ITEM_US = (By.XPATH,
                        '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/span[position()=1]')
ITEM_SELECT_US = (By.XPATH,
                           '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/span[position()=1]/select')
ITEM_INPUT_US = (By.XPATH,
                          '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/input')
ITEM_SUBMIT_US = (By.XPATH,
                           '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/div/span/span')
INVENTORY_TIPS_US = (By.XPATH,
                              '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div[position()=1]/div/div/div/span')
ITEM_DELETE_US = (By.XPATH,
                           '//*[@id=\'activeCartViewForm\']/div[position()=2]/div[position()=1]/div[position()=4]/div[position()=2]/div[position()=1]/div/div/div[position()=2]/div/span[position()=1]/span')

PRODUCT_ITEM_JP = (By.XPATH,
                        '//*[@id=\'activeCartViewForm\']/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div[position()=1]')
ITEM_SELECT_JP = (By.XPATH,
                           '//*[@id=\'activeCartViewForm\']/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/span[position()=1]/select[position()=1]')
ITEM_INPUT_JP = (By.XPATH,
                          '//*[@id=\'activeCartViewForm\']/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div[position()=1]/div[position()=4]/div/div[position()=3]/div/div[position()=1]/input[position()=1]')
ITEM_SUBMIT_JP = (By.ID, 'a-autoid-1')
INVENTORY_TIPS_JP = (By.XPATH,
                              '//*[@id=\'activeCartViewForm\']/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div[position()=1]/div[position()=4]/div[position()=1]/div/div/div/span')
ITEM_DELETE_JP = (By.XPATH,
                           '//*[@id=\'activeCartViewForm\']/div[position()=1]/div[position()=1]/div[position()=2]/div/div/div[position()=1]/div[position()=4]/div[position()=2]/div[position()=1]/div/div/div[position()=2]/div/span[position()=1]')

def getasinfromhref(template):
    rule = r'dp/(.*?)/ref'
    slotList = re.findall(rule, template)
    return slotList[0]

def test_node_gather():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        driver.get("https://www.amazon.com/gp/bestsellers/electronics/297859")
        for i in range(1, 50):
            item_symbol = item_prefix + str(i) + item_postfix
            element = driver.find_element_by_xpath(item_symbol)
            price = element.find_element_by_xpath(price_symbol)
            price_text = price.text
            href = element.find_element_by_xpath(href_symbol)
            asin_text = getasinfromhref(href.get_attribute("href"))
            review = element.find_element_by_xpath(review_symbol)
            review_text = review.text
            rate = element.find_element_by_xpath(rate_symbol)
            rate_text = rate.get_attribute("title").split(" ")[0]
            tmp = asin_text + " " + price_text.strip('$') + " " + review_text.replace(',', '') + " " + rate_text
            print(tmp, flush=True)
    except:
        print("xxxxxxx")
    finally:
        driver.quit()

def test_get_inventory_us():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        # driver.get("https://www.amazon.com/dp/B078H7VY19")
        driver.get("https://www.amazon.com/dp/B079NNC8N8")
        amazonasinpage = AmazonAsinPage(driver)
        if amazonasinpage.is_element_exsist(*FBA_FLAG):
            print("product is fba...", flush=True)
        else:
            print("product is fbm or not exsist...", flush=True)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(*QA_COUNT):
            element = driver.find_element(*QA_COUNT)
            print(element.text)
        else:
            print("qa_count not exsist...", flush=True)

        if amazonasinpage.is_element_exsist(*BUYER_COUNT):
            element = driver.find_element(*BUYER_COUNT)
            print(element.text)
        else:
            print("buy count no no", flush=True)

        amazonasinpage.add_cart(8000, 10000)

        if amazonasinpage.is_element_exsist(*NO_THANKS) == True:
            amazonasinpage.click(*NO_THANKS)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(*VIEW_CART_BUTTON):
            amazonasinpage.click(*VIEW_CART_BUTTON)
            amazonasinpage.random_sleep(8000, 10000)
        elif amazonasinpage.is_element_exsist(*VIEW_CART_BUTTON1):
            amazonasinpage.click(*VIEW_CART_BUTTON1)
            amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.select(9, *ITEM_SELECT_US)
        amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.input("999", *ITEM_INPUT_US)
        amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.click(*ITEM_SUBMIT_US)
        amazonasinpage.random_sleep(8000, 10000)

        element = driver.find_element(*INVENTORY_TIPS_US)
        print(element.text)

        amazonasinpage.click(*ITEM_DELETE_US)
    except NoSuchElementException as msg:
        print("Except: NoSuchElementException", flush=True)
    except Exception as e:
        print(e, flush=True)
    finally:
        input("xxx")
        driver.quit()

def test_get_inventory_jp():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        driver.get("https://www.amazon.co.jp/dp/B07BGXF6KF")
        amazonasinpage = AmazonAsinPage(driver)
        if amazonasinpage.is_element_exsist(*FBA_FLAG):
            print("product is fba...", flush=True)
        else:
            print("product is fbm or not exsist...", flush=True)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(*QA_COUNT):
            element = driver.find_element(*QA_COUNT)
            print(element.text)
        else:
            print("qa_count not exsist...", flush=True)

        if amazonasinpage.is_element_exsist(*BUYER_COUNT):
            element = driver.find_element(*BUYER_COUNT)
            print(element.text)
        else:
            print("buy count no no", flush=True)

        amazonasinpage.add_cart(8000, 10000)

        if amazonasinpage.is_element_exsist(*NO_THANKS) == True:
            amazonasinpage.click(*NO_THANKS)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(*VIEW_CART_BUTTON):
            amazonasinpage.click(*VIEW_CART_BUTTON)
            amazonasinpage.random_sleep(8000, 10000)
        elif amazonasinpage.is_element_exsist(*VIEW_CART_BUTTON1):
            amazonasinpage.click(*VIEW_CART_BUTTON1)
            amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.select(9, *ITEM_SELECT_JP)
        amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.input("999", *ITEM_INPUT_JP)
        amazonasinpage.random_sleep(8000, 10000)

        amazonasinpage.click(*ITEM_SUBMIT_JP)
        amazonasinpage.random_sleep(8000, 10000)

        element = driver.find_element(*INVENTORY_TIPS_JP)
        print(element.text)

        amazonasinpage.click(*ITEM_DELETE_JP)
    except NoSuchElementException as msg:
        print("Except: NoSuchElementException", flush=True)
    except Exception as e:
        print(e, flush=True)
    finally:
        input("xxx")
        driver.quit()

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    test_get_inventory_us()