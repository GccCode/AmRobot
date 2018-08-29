#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- encoding: utf-8 -*-

import  sys
import io
from selenium import webdriver
from amazonpage import AmazonPage
from amazonregisterpage import AmazonRegisterPage
from amazonaccountpage import AmazonAccountPage
from amazonaddresspage import AmazonAddressPage
from amazonpaymentpage import AmazonPaymentPage

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    status = 1
    while status == 1:
        print("本程序支持的测试路程如下：")
        print("0 - 退出测试")
        print("1 - 自动注册账号")
        print("2 - 自动登陆账号")
        print("3 - 自动添加物流地址")
        print("4 - 自动添加信用卡\n")

        options = input("请输入你的选择： ")
        if options == "0":
            status = 0
        elif options == "1":
            # option = webdriver.ChromeOptions()
            # option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            # driver = webdriver.Chrome(chrome_options=option)
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.enter_register_page(3000, 5000)
                registerpage = AmazonRegisterPage(driver)
                registerpage.sign_in(3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.quit()
        elif options == "2":
            pass
        elif options == "3":
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                print("支持收货地址类型如下：")
                print("1 - 账单地址")
                print("2 - FBA地址")
                addressoption = input("请输入你的选择： ")

                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.enter_account_page(3000,5000)
                accountpage = AmazonAccountPage(driver)
                accountpage.enter_address_page(3000, 5000)
                addresspage = AmazonAddressPage(driver)
                if addressoption == "1":
                    addresspage.add_address("bill", 3000, 5000)
                elif addressoption == "2":
                    addresspage.add_address("fba", 3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.quit()
        elif options == "4":
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            # driver = webdriver.Chrome()
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.enter_account_page(3000, 5000)
                accountpage = AmazonAccountPage(driver)
                accountpage.enter_payment_page(3000, 5000)
                paymentpage = AmazonPaymentPage(driver)
                paymentpage.add_new_payment(3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.quit()
        else:
            print("你的输入有误，请重新输入对应测试项的数字号码！！！！")