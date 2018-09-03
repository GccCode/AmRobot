#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import base64
import sys
import io

def encry(cnf_org, cnf_encry):
    f_org = open(cnf_org, 'r')
    content = f_org.read()
    content1 = content.encode(encoding='utf-8')
    content2 = base64.b64encode(content1)
    #print("加密后内容：\n")
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

def keep_input_bool(content):
    count = 0
    while True:
        value = input(content)
        if value == "0" or value == "1":
            return value
        else:
            count += 1
            if count == 4:
                sys.exit(1)
            else:
                print("输入有误，请重新输入次数：" + str(4 - count) + " \n")

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
    status = True
    while status == True:
        print("\n========== 主菜单 ============")
        action = input("* 退出-0, 配置-1，解密文件-2：")
        if action == "0":
            status = False
        elif action == "1":
            print("\n========== 配置菜单 ============")
            cfgtype = input("** 退出-0，设置账号-1，设置动作-2：")
            if cfgtype == "1":
                cf = configparser.ConfigParser()
                cf.add_section("broswer")
                print("\n==== 配置浏览器 ====\n")
                broswer = input("*** 请输入浏览器类型（谷歌-1，火狐-2）：")
                if (broswer != "2") and (broswer != "1"):
                    print("输入有误！！！！只能为0或者1\n")
                else:
                    cf.set("broswer", "type", broswer)
                    print("\n==== 配置代理 ====\n")
                    host_ip = input("*** 请输入代理ip端口（格式：IP:端口，直接跳过请输入0）：")
                    if host_ip != "0":
                        cf.add_section("proxy")
                        cf.set("proxy", "proxy", host_ip)
                    print("\n==== 配置登陆账号 ====\n")
                    cf.add_section("account")
                    country = input("*** 请输入账号国家（美国-us，日本-jp)：")
                    cf.set("account", "country", country)
                    username = input("*** 请输入用户名：")
                    cf.set("account", "username", username)
                    if country == "jp":
                        pronunciation = input("*** 请输入日本平假名：")
                        cf.set("account", "pronunciation", pronunciation)
                    email = input("*** 请输入邮箱地址：")
                    cf.set("account", "email", email)
                    password = input("*** 请输入密码：")
                    cf.set("account", "password", password)
                    print("\n==== 配置账单地址 ====\n")
                    cf.add_section("bill_address")
                    fullname = input("*** 请输入全名：")
                    cf.set("bill_address", "fullname", fullname)
                    addressline1 = input("*** 请输入地址行：")
                    cf.set("bill_address", "addressline1", addressline1)
                    if country == "jp":
                        addressline2 = input("*** 日本账号需要补齐地址行2：")
                        cf.set("bill_address", "addressline2", addressline2)
                    city = input("*** 请输入城市：")
                    cf.set("bill_address", "city", city)
                    state = input("*** 请输入州县：")
                    cf.set("bill_address", "state", state)
                    if country == "us":
                        postalcode = input("*** 请输入邮编：")
                        cf.set("bill_address", "postalcode", postalcode)
                    elif country == "jp":
                        postalcode1 = input("*** 请输入日本邮编1：")
                        cf.set("bill_address", "postalcode1", postalcode1)
                        postalcode2 = input("*** 请输入日本邮编2：")
                        cf.set("bill_address", "postalcode2", postalcode1)
                    phone = input("*** 请输入电话号码：")
                    cf.set("bill_address", "phone", phone)
                    print("\n==== 配置收货地址 ====\n")
                    cf.add_section("fba_address")
                    fullname = input("*** 请输入全名：")
                    cf.set("fba_address", "fullname", fullname)
                    addressline1 = input("*** 请输入地址行：")
                    cf.set("fba_address", "addressline1", addressline1)
                    if country == "jp":
                        addressline2 = input("*** 日本账号需要补齐地址行2：")
                        cf.set("fba_address", "addressline2", addressline2)
                    city = input("*** 请输入城市：")
                    cf.set("fba_address", "city", city)
                    state = input("*** 请输入州县：")
                    cf.set("fba_address", "state", state)
                    if country == "us":
                        postalcode = input("*** 请输入邮编：")
                        cf.set("fba_address", "postalcode", postalcode)
                    elif country == "jp":
                        postalcode1 = input("*** 请输入日本邮编1：")
                        cf.set("fba_address", "postalcode1", postalcode1)
                        postalcode2 = input("*** 请输入日本邮编2：")
                        cf.set("fba_address", "postalcode2", postalcode1)
                    phone = input("*** 请输入电话号码：")
                    cf.set("fba_address", "phone", phone)
                    print("\n==== 配置卡信息 ====\n")
                    cf.add_section("cardinfo")
                    cardnumber = input("*** 请输入卡号：")
                    cf.set("cardinfo", "cardnumber", cardnumber)
                    month = input("*** 请输入卡的有效月份：")
                    cf.set("cardinfo", "month", month)
                    year = input("*** 请输入卡的有效年份：")
                    cf.set("cardinfo", "year", year)

                    store = keep_input_bool("*** 退出-0，保存设置文件-1，请输入：")
                    if store == "0":
                        status = False
                    else:
                        filename = input("请输入保存文件名：")
                        cf.write(open((filename + ".txt"), 'w'))
                        encry((filename + ".txt"), ("_" + filename + ".txt"))
            elif cfgtype == "2":
                cf = configparser.ConfigParser()
                register = keep_input_bool("*** 是否注册账号（否-0，是-1)：")
                cf.add_section("register")
                cf.set("register", "status", register)

                login = keep_input_bool("*** 是否登陆账号（否-0，是-1)：")
                cf.add_section("login")
                cf.set("login", "status", login)

                bill_address = keep_input_bool("*** 是否添加账单地址（否-0，是-1)：")
                cf.add_section("bill_address")
                cf.set("bill_address", "status", bill_address)
                cf.set("bill_address", "type", "0")

                card = keep_input_bool("*** 是否添加卡（否-0，是-1)：")
                cf.add_section("card")
                cf.set("card", "status", card)

                fba_address = keep_input_bool("*** 是否添加收货地址（否-0，是-1)：")
                cf.add_section("fba_address")
                cf.set("fba_address", "status", fba_address)
                cf.set("fba_address", "type", "1")

                prime = keep_input_bool("*** 是否注册会员（否-0，是-1)：")
                cf.add_section("prime")
                cf.set("prime", "status", prime)

                random_view = keep_input_bool("*** 是否浏览关键词任意产品（否-0，是-1)：")
                cf.add_section("random_view")
                cf.set("random_view", "status", random_view)
                if random_view == "1":
                    keyword = input("**** 请输入关键词：")
                    cf.set("random_view", "keyword", keyword)
                elif random_view == "0":
                    cf.add_section("super_link")
                    super_link = keep_input_bool("*** 是否浏览超链接（否-0，是-1）：")
                    cf.set("super_link", "status", super_link)
                    if super_link == "1":
                        link = input("**** 超链接：")
                        cf.set("super_link", "link", link)
                        cf.add_section("review_view")
                        review_view = keep_input_bool("**** 是否浏览评论（否-0，是-1）：")
                        cf.set("review_view", "status", review_view)

                        cf.add_section("qa_submit")
                        qa_submit = keep_input_bool("**** 是否提交QA（否-0，是-1）：")
                        cf.set("qa_submit", "status", qa_submit)
                        if qa_submit == "1":
                            content = input("***** 请输入QA内容：")
                            cf.set("qa_submit", "content", content)

                        cf.add_section("wishlist")
                        wishlist = keep_input_bool("**** 是否加心愿卡（否-0，是-1）：")
                        cf.set("wishlist", "status", wishlist)

                        cf.add_section("addcart")
                        addcart = keep_input_bool("**** 是否加购物车（否-0，是-1）：")
                        cf.set("addcart", "status", addcart)
                    else:
                        cf.add_section("search")
                        search = keep_input_bool("*** 是否搜索关键词产品（否-0，是-1：")
                        cf.set("search", "status", search)
                        if search == "1":
                            keyword = input("**** 请输入关键词：")
                            cf.set("search", "keyword", keyword)
                            condition = keep_input_bool("**** 是否手动卡位（否-0，是-1）：")
                            cf.set("search", "condition_setup", condition)
                            variation = keep_input_bool("**** 是否手动选择变体（否-0，是-1）：")
                            cf.set("search", "variation_setup", variation)
                            asin = input("**** 请输入产品ASIN：")
                            cf.set("search", "asin", asin)
                            type = input("**** 请输入产品入口（广告-0，普通-1）：")
                            cf.set("search", "type", type)
                            page = input("**** 产品大概是几页内：")
                            cf.set("search", "page", page)

                            cf.add_section("review_view")
                            review_view = keep_input_bool("**** 是否浏览评论（否-0，是-1）：")
                            cf.set("review_view", "status", review_view)

                            cf.add_section("qa_submit")
                            qa_submit = keep_input_bool("**** 是否提交QA（否-0，是-1）：")
                            cf.set("qa_submit", "status", qa_submit)
                            if qa_submit == "1":
                                content = input("***** 请输入QA内容：")
                                cf.set("qa_submit", "content", content)

                            cf.add_section("wishlist")
                            wishlist = keep_input_bool("**** 是否加心愿卡（否-0，是-1）：")
                            cf.set("wishlist", "status", wishlist)

                            cf.add_section("addcart")
                            addcart = keep_input_bool("**** 是否加购物车（否-0，是-1）：")
                            cf.set("addcart", "status", addcart)

                store = keep_input_bool("退出-0，保存设置文件-1，请输入：")
                if store == "0":
                    status = False
                else:
                    filename = input("请输入保存文件名：")
                    cf.write(open((filename + ".txt"), 'w'))
                    encry((filename + ".txt"),(filename + "-encry.txt"))

        elif action == "2":
            print("\n========== 解密文件菜单 ============")
            filename = input("请输入解密文件名：")
            deci((filename + ".txt"), ("deci-" + filename + ".txt"))









