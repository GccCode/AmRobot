#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- encoding: utf-8 -*-

import  sys
import io
import random
import os
import time as tm
import base64
import configparser
from selenium import webdriver
from amazonpage import AmazonPage
from amazonregisterpage import AmazonRegisterPage
from amazonaccountpage import AmazonAccountPage
from amazonaddresspage import AmazonAddressPage
from amazonpaymentpage import AmazonPaymentPage
from amazonsigninpage import AmazonSignInPage
from amazonsearchpage import  AmazonSearchPage
from amazonasinpage import  AmazonAsinPage


def encry(cnf_org, cnf_encry):
    f_org = open(cnf_org, 'r')
    content = f_org.read()
    content1 = content.encode(encoding='utf-8')
    content2 = base64.b64encode(content1)
    print("加密后内容：\n")
    print(content2)
    f_org.close()
    with open(cnf_encry, 'wb+') as f_org:
        f_org.write(content2)


def deci(cnf_now, cnf_deci):
    f_now = open(cnf_now, 'r')
    content = f_now.read()
    content1 = base64.b64decode((content))
    print("解密后内容：\n")
    print(content1)
    with open(cnf_deci, 'wb+') as f_now:
        f_now.write(content1)

def customized_broswer():
    cf = configparser.ConfigParser()
    cf.read("info.txt")
    option = webdriver.ChromeOptions()
    status = cf.get("proxy", "status")
    if status == "1":
        host_port = cf.get("proxy", "proxy")
        proxy_socks_argument = '--proxy-server=socks5://' + host_port
        option.add_argument(proxy_socks_argument)
    ua = cf.get("broswer", "type")
    if ua == "2":
        option.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0')
    option.add_argument(
        r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
    return webdriver.Chrome(chrome_options=option)

if __name__ == "__main__":
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
    while True:
        print("========= 程序功能选择 ========\n")
        print("0. 退出\n")
        print("1. 单独操作\n")
        print("2. 批量操作\n")
        action = input("请选择：")
        if action == "0":
            break
        elif action == "1":
            while True:
                print("==========本程序支持的测试功能如下==========")
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
                print("10 - 添加QA内容")
                print("11 - 代理测试\n")

                options = input("请输入你的选择： ")
                if options == "0":
                    break
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
                            page.search_asin(keyword, 5000, 8000)
                            currenthandle = page.get_currenthandle()
                            searchpage = AmazonSearchPage(driver)
                            asinresult = searchpage.find_target_product(asin, type, 5)
                            if asinresult != False:
                                if searchpage.is_asin_sponsored(asinresult, asin):
                                    print("the item is sponsored..\n")
                                if searchpage.is_asin_amazon_choice(asinresult, asin):
                                    print("the item is amazon choice..\n")
                                t1 = tm.time()
                                searchpage.enter_random_product(asin, random.randint(10, 20), 3000, 5000)
                                t2 = tm.time()
                                print("第1次货比耗时" + format(t2 - t1))
                                t1 = tm.time()
                                searchpage.enter_random_product(asin, random.randint(10, 20), 3000, 5000)
                                t2 = tm.time()
                                print("第2次货比耗时" + format(t2 - t1))
                                asinresult = searchpage.find_target_product(asin, type, 5)
                                if asinresult != False:
                                    searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                                    t1 = tm.time()
                                    page.random_walk(random.randint(30, 60))
                                    t2 = tm.time()
                                    print("浏览产品耗时：" + format(t2 - t1))
                                    searchpage.back_prev_page_by_country(currenthandle, 3000, 5000)
                                else:
                                    print("找不到产品！！！！\n")

                        except Exception as err:
                            print(str(err))
                        finally:
                            input("请按回车键继续推出！")
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
                            currenthandle = page.get_currenthandle()
                            searchpage = AmazonSearchPage(driver)
                            asinresult = searchpage.find_target_product(asin, type, 5)
                            if asinresult != False:
                                searchpage.enter_asin_page(asinresult, asin, 5000, 10000)
                                asinpage = AmazonAsinPage(driver)
                                searchpage.switch_to_new_page(currenthandle)
                                asinpage.add_wishlist(5000, 8000)
                                searchpage.back_prev_page_by_type(currenthandle, "current", 3000, 5000)

                        except Exception as err:
                            print(str(err))
                        finally:
                            input("请按回车键继续推出！！！")
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
                            currenthandle = page.get_currenthandle()
                            searchpage = AmazonSearchPage(driver)
                            asinresult = searchpage.find_target_product(asin, type, 5)
                            if asinresult != False:
                                searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                                asinpage = AmazonAsinPage(driver)
                                searchpage.switch_to_new_page(currenthandle)
                                asinpage.add_cart(3000, 5000)
                                searchpage.back_prev_page_by_type(currenthandle, "current", 3000, 5000)

                        except Exception as err:
                            print(str(err))
                        finally:
                            input("请按回车键继续推出！！！")
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
                            currenthandle = page.get_currenthandle()
                            searchpage = AmazonSearchPage(driver)
                            asinresult = searchpage.find_target_product(asin, type, 5)
                            if asinresult != False:
                                searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                                asinpage = AmazonAsinPage(driver)
                                searchpage.switch_to_new_page(currenthandle)
                                asinpage.ask_qa(content, 3000, 5000)
                                searchpage.back_prev_page_by_type(currenthandle, "current", 3000, 5000)

                        except Exception as err:
                            print(str(err))
                        finally:
                            input("请按回车键继续推出！！！")
                            driver.close()
                            driver.quit()
                elif options == "11":
                    host_port = input("请输入ip-port：")
                    ua = input("请选择UserAgent：")
                    proxy_socks_argument = '--proxy-server=socks5://' + host_port
                    print(proxy_socks_argument)
                    option = webdriver.ChromeOptions()
                    option.add_argument(proxy_socks_argument)
                    if ua == "1":
                        option.add_argument('--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
                    elif ua == "2":
                        option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0')
                    elif ua == "3":
                        option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
                    elif ua == "4":
                        option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
                    else:
                        option.add_argument(
                            r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
                    driver = webdriver.Chrome(chrome_options=option)
                    driver.get("http://www.whatsmyuseragent.com/")
                    input("按下回车键关闭浏览器....")
                    driver.close()
                    driver.quit()
                else:
                    print("你的输入有误，请重新输入对应测试项的数字号码！！！！")
        elif action == "2":
            try:
                t1 = tm.time()
                driver = customized_broswer()
                driver.set_page_load_timeout(60)
                driver.set_script_timeout(60)
                # deci("_task.txt", "task.txt")
                cf = configparser.ConfigParser()
                cf.read("task.txt")
                #os.remove("task.txt")
                amazonpage = AmazonPage(driver)
                register = cf.get("register", "status")
                if register == "1":
                    amazonpage.enter_amazon_page(3000, 5000)
                    amazonpage.enter_register_page(3000, 5000)
                    registerpage = AmazonRegisterPage(driver)
                    registerpage.register(5000, 10000)
                login = cf.get("login", "status")
                if login == "1":
                    amazonpage.enter_amazon_page(3000, 5000)
                    amazonpage.enter_signin_page(3000, 5000)
                    signinpage = AmazonSignInPage(driver)
                    signinpage.sign_in(5000, 10000)
                bill_address = cf.get("bill_address", "status")
                if bill_address == "1":
                    type = cf.get("bill_address", "type")
                    amazonpage.enter_account_page(3000, 5000)
                    accountpage = AmazonAccountPage(driver)
                    accountpage.enter_address_page(3000, 5000)
                    addresspage = AmazonAddressPage(driver)
                    addresspage.add_address("bill", 5000, 10000)
                card = cf.get("card", "status")
                if card == "1":
                    amazonpage.enter_account_page(3000, 5000)
                    accountpage = AmazonAccountPage(driver)
                    accountpage.enter_payment_page(3000, 5000)
                    paymentpage = AmazonPaymentPage(driver)
                    paymentpage.add_new_payment(5000, 10000)
                fba_address = cf.get("fba_address", "status")
                if fba_address == "1":
                    type = cf.get("fba_address", "type")
                    amazonpage.enter_account_page(3000, 5000)
                    accountpage = AmazonAccountPage(driver)
                    accountpage.enter_address_page(3000, 5000)
                    addresspage = AmazonAddressPage(driver)
                    addresspage.add_address("fba", 5000, 10000)
                prime = cf.get("prime", "status")
                if prime == "1":
                    amazonpage.enter_amazon_page(3000, 5000)
                    amazonpage.register_prime(5000, 10000)
                random_view = cf.get("random_view", "status")
                if random_view == "1":
                    keyword = cf.get("random_view", "keyword")
                    amazonpage.search_asin(keyword, 5000, 8000)
                    searchpage = AmazonSearchPage(driver)
                    searchpage.enter_random_products(3, random.randint(15, 30), 3000, 5000)
                else:
                    searchpage = AmazonSearchPage(driver)
                    search = cf.get("search", "status")
                    searchpage_handle = 0
                    if search == "1":
                        super_link = cf.get("super_link", "status")
                        if super_link == "1":
                            link = cf.get("super_link", "link")
                            amazonpage.enter_super_link(link, 3000, 5000)
                            searchpage_handle = amazonpage.get_currenthandle()
                        else:
                            keyword = cf.get("search", "keyword")
                            amazonpage.search_asin(keyword, 5000, 8000)
                            searchpage_handle = amazonpage.get_currenthandle()
                            condition_setup = cf.get("search", "condition_setup")
                            if condition_setup == "1":
                                input("请进行手动卡位，完成后按回车键继续自动搜索产品！！！")
                            page = cf.get("search", "page")
                            asin = cf.get("search", "asin")
                            type = cf.get("search", "type")
                            if type == "0":
                                entry_type = "sponsored"
                            elif type == "1":
                                entry_type = "normal"
                            asinresult = searchpage.find_target_product(asin, entry_type, int(page))
                            if asinresult != False:
                                searchpage.enter_random_products(asinresult, random.randint(2, 3), random.randint(8, 15), 5000, 8000)
                                asinresult = searchpage.find_target_product(asin, entry_type, int(page))
                                if asinresult != False:
                                    searchpage.enter_asin_page(asinresult, asin, 3000, 5000)
                                else:
                                    print("找不到产品！！！！\n")
                                    sys.exit(1)

                        variation_setup = cf.get("search", "variation_setup")
                        if variation_setup == "1":
                            input("请进行手动选择目标变体，完成后按回车键继续自动化！！！：")

                        amazonpage.random_walk(random.randint(35, 50))
                        asinpage = AmazonAsinPage(driver)
                        searchpage.switch_to_new_page(searchpage_handle) #切换到产品页handle

                        review_view = cf.get("review_view", "status")
                        if review_view == "1":
                            asinpage.review_all(3000, 5000)
                            amazonpage.navigation_back(3000, 5000)
                        qa_submit = cf.get("qa_submit", "status")
                        if qa_submit == "1":
                            content = cf.get("qa_submit", "content")
                            asinpage.ask_qa(content, 3000, 5000)
                            amazonpage.navigation_back(3000, 5000)

                        wishlist = cf.get("wishlist", "status")
                        if wishlist == "1":
                            asinpage.add_wishlist(5000, 8000)

                        addcart = cf.get("addcart", "status")
                        if addcart == "1":
                            asinpage.add_cart(3000, 5000)

                        searchpage.back_prev_page_by_country(searchpage_handle, 3000, 5000)
                        random_status = random.randint(1, 200)
                        if (random_status % 2) == 1:
                            amazonpage.random_walk(random.randint(2, 7))
                        else:
                            print("随机数是：" + str(random_status) + "\n")
            except Exception as err:
                print(str(err))
            finally:
                t2 = tm.time()
                print("总耗时：" + format(t2 - t1))
                input("请按回车键继续退出程序！！！")
                driver.close()
                driver.quit()
        else:
            print("你的输入有误，请重新输入对应测试项的数字号码！！！！")