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
from amazonsigninpage import AmazonSignInPage
from amazonsearchpage import  AmazonSearchPage
from amazonasinpage import  AmazonAsinPage


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    status = 1
    while status == 1:
        print("==========本程序支持的测试路程如下==========")
        print("0 - 退出测试")
        print("1 - 自动注册账号")
        print("2 - 自动登陆账号")
        print("3 - 自动添加物流地址")
        print("4 - 自动添加信用卡")
        print("5 - 打开浏览器")
        print("6 - 搜索关键词")
        print("7 - 自动注册会员")
        print("8 - 添加心愿卡")
        print("9 - 添加购物车")
        print("10 - 添加QA内容\n")

        options = input("请输入你的选择： ")
        if options == "0":
            status = 0
        elif options == "1":
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.enter_register_page(3000, 5000)
                registerpage = AmazonRegisterPage(driver)
                registerpage.register(3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.close()
                driver.quit()
        elif options == "2":
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.enter_signin_page(3000, 5000)
                signinpage = AmazonSignInPage(driver)
                signinpage.sign_in(3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.close()
                driver.quit()

        elif options == "3":
            print("支持收货地址类型如下：")
            print("1 - 账单地址")
            print("2 - FBA地址")
            addressoption = input("请输入你的选择： ")
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
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
                driver.close()
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
                driver.close()
                driver.quit()
        elif options == "5":
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            input("按下回车键关闭浏览器....\n")
            driver.close()
            driver.quit()
        elif options == "6":
            keyword = input("请输入想要搜索的关键词： ")
            asin = input("请输入搜索产品的ASIN： ")
            typestr = input("请输入目标产品类型对应数字（广告-0 or 普通-1）：")
            type = ""
            if typestr == "0":
                type = "sponsored"
            elif typestr == "1":
                type = "normal"
            else:
                print("你的输入有误！！！！\n")
            if typestr == "0" or typestr == "1":
                option = webdriver.ChromeOptions()
                option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
                driver = webdriver.Chrome(chrome_options=option)
                driver.set_page_load_timeout(30)
                driver.set_script_timeout(30)
                try:
                    # keyword = "echo dot 壁掛け"
                    # asin = "B07BBL5T2P"
                    # asin = "B07CQYCJ7B"
                    # asin = "B07BGXF6KF"
                    # asin = "B072B5BTLK"

                    # keyword = "gold plastic cups"
                    #asin = "B07G2R3Y5J"
                    # asin = "B07CGMVGNG"
                    #asin = "B004UUK2ZY"
                    #asin = "B079YY714G"
                    page = AmazonPage(driver)
                    page.enter_amazon_page(3000, 5000)
                    page.search_asin(keyword, 3000, 5000)
                    searchpage = AmazonSearchPage(driver)
                    asinresult = searchpage.find_target_product(asin, type)
                    if asinresult != False:
                        if searchpage.is_asin_sponsored(asinresult, asin):
                            print("the item is sponsored..\n")
                        if searchpage.is_asin_amazon_choice(asinresult, asin):
                            print("the item is amazon choice..\n")
                        searchpage.enter_random_product(asin, 3000, 5000)
                        searchpage.enter_random_product(asin, 3000, 5000)
                        asinresult = searchpage.find_target_product(asin, type)
                        if asinresult != False:
                            currenthandle= searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                            searchpage.back_prev_page(currenthandle, 3000, 5000)
                            searchpage.enter_next_page(3000, 5000)
                            searchpage.enter_random_products(3, 3000, 5000)
                            page.random_walk(5)

                except Exception as err:
                    print(str(err))
                finally:
                    driver.close()
                    driver.quit()
        elif options == "7":
            option = webdriver.ChromeOptions()
            option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
            driver = webdriver.Chrome(chrome_options=option)
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            try:
                page = AmazonPage(driver)
                page.enter_amazon_page(3000, 5000)
                page.register_prime(3000, 5000)
            except Exception as err:
                print(str(err))
            finally:
                driver.close()
                driver.quit()
        elif options == "8":
            keyword = input("请输入想要搜索的关键词： ")
            asin = input("请输入搜索产品的ASIN： ")
            typestr = input("请输入目标产品类型对应数字（广告-0 or 普通-1）：")
            type = ""
            if typestr == "0":
                type = "sponsored"
            elif typestr == "1":
                type = "normal"
            else:
                print("你的输入有误！！！！\n")
            if typestr == "0" or typestr == "1":
                option = webdriver.ChromeOptions()
                option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
                driver = webdriver.Chrome(chrome_options=option)
                driver.set_page_load_timeout(30)
                driver.set_script_timeout(30)
                try:
                    page = AmazonPage(driver)
                    page.enter_amazon_page(3000, 5000)
                    page.search_asin(keyword, 3000, 5000)
                    searchpage = AmazonSearchPage(driver)
                    asinresult = searchpage.find_target_product(asin, type)
                    if asinresult != False:
                        currenthandle= searchpage.enter_asin_page(asinresult, asin, 5000, 10000)
                        asinpage = AmazonAsinPage(driver)
                        asinpage.add_wishlist(5000, 8000)

                except Exception as err:
                    print(str(err))
                finally:
                    driver.close()
                    driver.quit()
        elif options == "9":
            keyword = input("请输入想要搜索的关键词： ")
            asin = input("请输入搜索产品的ASIN： ")
            typestr = input("请输入目标产品类型对应数字（广告-0 or 普通-1）：")
            type = ""
            if typestr == "0":
                type = "sponsored"
            elif typestr == "1":
                type = "normal"
            else:
                print("你的输入有误！！！！\n")
            if typestr == "0" or typestr == "1":
                option = webdriver.ChromeOptions()
                option.add_argument(
                    r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
                driver = webdriver.Chrome(chrome_options=option)
                driver.set_page_load_timeout(30)
                driver.set_script_timeout(30)
                try:
                    page = AmazonPage(driver)
                    page.enter_amazon_page(3000, 5000)
                    page.search_asin(keyword, 3000, 5000)
                    searchpage = AmazonSearchPage(driver)
                    asinresult = searchpage.find_target_product(asin, type)
                    if asinresult != False:
                        currenthandle = searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                        asinpage = AmazonAsinPage(driver)
                        asinpage.add_cart(3000, 5000)

                except Exception as err:
                    print(str(err))
                finally:
                    driver.close()
                    driver.quit()
        elif options == "10":
            keyword = input("请输入想要搜索的关键词： ")
            asin = input("请输入搜索产品的ASIN： ")
            typestr = input("请输入目标产品类型对应数字（广告-0 or 普通-1）：")
            content = input("请输入要提交的QA内容：")
            type = ""
            if typestr == "0":
                type = "sponsored"
            elif typestr == "1":
                type = "normal"
            else:
                print("你的输入有误！！！！\n")
            if typestr == "0" or typestr == "1":
                option = webdriver.ChromeOptions()
                option.add_argument(
                    r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
                driver = webdriver.Chrome(chrome_options=option)
                driver.set_page_load_timeout(30)
                driver.set_script_timeout(30)
                try:
                    page = AmazonPage(driver)
                    page.enter_amazon_page(3000, 5000)
                    page.search_asin(keyword, 3000, 5000)
                    searchpage = AmazonSearchPage(driver)
                    asinresult = searchpage.find_target_product(asin, type)
                    if asinresult != False:
                        currenthandle = searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                        asinpage = AmazonAsinPage(driver)
                        asinpage.ask_qa(content, 3000, 5000)

                except Exception as err:
                    print(str(err))
                finally:
                    driver.close()
                    driver.quit()
        else:
            print("你的输入有误，请重新输入对应测试项的数字号码！！！！")