#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import re
import sys
import io
from selenium.webdriver.common.by import By
from amazonasinpage import AmazonAsinPage
from selenium.common.exceptions import NoSuchElementException


item_prefix = "//*[@id='zg-ordered-list']/li[position()="
item_postfix = "]/span"
price_symbol = ".//div/span/div[position()=2]/a[position()=1]/span/span"
review_symbol = ".//div/span/div[position()=1]/a[position()=2]"
href_symbol = ".//div/span/div[position()=2]/a[position()=1]"
rate_symbol = ".//div/span/div[position()=1]/a"
BUYER_COUNT = (By.XPATH, "//*[@id='olp_feature_div']/div/span[position()=1]/a")
QA_COUNT = (By.ID, "askATFLink")
QA_COUNT1 = (By.XPATH, "//*[@id='askATFLink']/span")
FBA_FLAG = (By.ID, "SSOFpopoverLink")

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

def test_get_inventory():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        driver.get("https://www.amazon.com/dp/B078H7VY19")
        amazonasinpage = AmazonAsinPage(driver)
        if amazonasinpage.is_element_exsist(FBA_FLAG):
            print("product is fba...", flush=True)
        else:
            print("product is fbm or not exsist...", flush=True)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(QA_COUNT):
            element = driver.find_element_by_id("askATFLink")
            element.find_element_by_xpath(".//span")
            print("aaa")
            print(element.text)
        else:
            print("qa_count not exsist...", flush=True)

        amazonasinpage.add_cart(8000, 10000)

        NO_THANKS = (By.ID, 'attachSiNoCoverage')
        VIEW_CART_BUTTON = (By.ID, 'attach-sidesheet-view-cart-button')
        if amazonasinpage.is_element_exsist(NO_THANKS):
            print("no thanks", flush=True)
        else:
            print("no no thanks")

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(VIEW_CART_BUTTON):
            print("llll", flush=True)
        else:
            print("222", flush=True)
    except NoSuchElementException as msg:
        status = False
        print("Except: NoSuchElementException", flush=True)
    except:
        print("xxxx", flush=True)
    finally:
        driver.quit()

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        driver.get("https://www.amazon.com/dp/B078H7VY19")
        amazonasinpage = AmazonAsinPage(driver)
        if amazonasinpage.is_element_exsist(FBA_FLAG):
            print("product is fba...", flush=True)
        else:
            print("product is fbm or not exsist...", flush=True)

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(QA_COUNT):
            element = driver.find_element_by_id("askATFLink")
            element.find_element_by_xpath(".//span")
            print("aaa")
            print(element.text)
        else:
            print("qa_count not exsist...", flush=True)

        amazonasinpage.add_cart(8000, 10000)

        NO_THANKS = (By.ID, 'attachSiNoCoverage')
        VIEW_CART_BUTTON = (By.ID, 'attach-sidesheet-view-cart-button')
        if amazonasinpage.is_element_exsist(NO_THANKS):
            print("no thanks", flush=True)
        else:
            print("no no thanks")

        amazonasinpage.random_sleep(1000, 2000)
        if amazonasinpage.is_element_exsist(VIEW_CART_BUTTON):
            print("llll", flush=True)
        else:
            print("222", flush=True)
    except NoSuchElementException as msg:
        status = False
        print("Except: NoSuchElementException", flush=True)
    except Exception as e:
        print(e, flush=True)
    finally:
        driver.quit()