#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import string
import os
import time
import requests
import sys
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import re
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
import os, win32gui, win32ui, win32con, win32api

#0)
#1) Chrome
#2) Firefox+Win7:
#3) Safari+Win7:
#4) Opera+Win7:
#5) IE+Win7+ie9：
#6) Win7+ie8：
#7) WinXP+ie8：
#8) WinXP+ie7：
#9) WinXP+ie6：
useragentlist = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
]

def getfilelines(filename, eol='\n', buffsize=4096):
    """计算给定文件有多少行"""
    with open(filename, 'rb') as handle:
        linenum = 0
        buffer = handle.read(buffsize)
        while buffer:
            linenum += buffer.count(bytes(eol, encoding='utf-8'))
            buffer = handle.read(buffsize)
        return linenum


def readtline(filename, lineno, eol="\n", buffsize=4096):
    """读取文件的指定行"""
    with open(filename, 'rb') as handle:
        readedlines = 0
        buffer = handle.read(buffsize)
        while buffer:
            thisblock = buffer.count(bytes(eol, encoding='utf-8'))
            if readedlines < lineno < readedlines + thisblock:
                # inthisblock: findthe line content, and return it
                return buffer.split(bytes(eol, encoding='utf-8'))[lineno - readedlines - 1]
            elif lineno == readedlines + thisblock:
                # need continue read line rest part
                part0 = buffer.split(bytes(eol, encoding='utf-8'))[-1]
                buffer = handle.read(buffsize)
                part1 = buffer.split(bytes(eol, encoding='utf-8'))[0]
                return part0 + part1
            readedlines += thisblock
            buffer = handle.read(buffsize)
        else:
            raise IndexError


def getrandomline(filename):
    """读取文件的任意一行"""
    import random
    return readtline(
        filename,
        random.randint(0, getfilelines(filename)),
    ).decode().strip().title()

def change_proxy():
    cur_cwd = os.getcwd()
    os.chdir("D:\Program Files\911S5 2018-05-23 fixed\ProxyTool")
    os.popen("Autoproxytool.exe -changeproxy/US/CA")
    os.chdir(cur_cwd)
    time.sleep(5)
    print(("* 切换代理ip。。。"), flush=True)

def generate_username():
    return (getrandomline('usernames') + " " + getrandomline('usernames'))


def generate_password():
    #candidates = string.digits + string.ascii_letters + '!@$%&*+-_'
    candidates = string.digits + string.ascii_letters + '!@'
    passwd = ''
    for i in range(random.randint(8, 14)):
        passwd += random.choice(candidates)

    return passwd


def generate_email():
    prefix = string.digits + string.ascii_lowercase
    postfix = ['@yahoo.com', '@outlook.com', '@hotmail.com', '@gmail.com']
    prefix_len = random.randint(5, 12)
    mail = ''
    for i in range(prefix_len):
        mail += random.choice(prefix)
    return (getrandomline('usernames') + mail + random.choice(postfix))



def generate_address():
    url = r'https://fakena.me/random-real-address/'
    referer = r'https://fakena.me'
    header = {'user-agent': generate_user_agent(), 'referer': referer}
    text = requests.get(url, headers=header).text
    pattern = re.compile('<strong>(.+)<br>(.+)</strong>')
    result = re.findall(pattern, text)
    if result:  # sometimes the result is empty
        address_line = result[0][0]
        city, state_zip = result[0][1].split(',')
        state, zip = state_zip.split()
        format_addr = [address_line, city, state, zip]
        return format_addr
    else:
        return ''


def generate_card():
    url = r'http://www.fakeaddressgenerator.com/World/us_address_generator'
    referer = r'http://www.fakeaddressgenerator.com/World'
    header = {'user-agent': generate_user_agent(), 'referer': referer}
    text = requests.get(url, headers=header).text
    soup = BeautifulSoup(text, 'lxml')
    info = soup.find_all('input')
    # for i in range(0, 25):
    #     print(str(i) + " : " + info[i]['value'])
    # name_phone = info[0]['value'] + '#' + info[9]['value']
    # name_visa = info[0]['value'] + '#' + info[11]['value'] + '#' + info[13]['value']
    return [info[5]['value'], info[21]['value'], info[23]['value']]

def generate_info_file():
    cf_info = configparser.ConfigParser()
    cf_info.add_section("account")
    cf_info.set("account", "country", "us")
    username = generate_username()
    cf_info.set("account", "username", username)
    email = generate_email()
    cf_info.set("account", "email", email)
    password = generate_password()
    cf_info.set("account", "password", password)
    cf_info.add_section("bill_address")
    cf_info.set("bill_address", "fullname", username)
    address = generate_address()
    line = address[0]
    cf_info.set("bill_address", "addressline1", line)
    city = address[1]
    cf_info.set("bill_address", "city", city)
    state = address[2]
    cf_info.set("bill_address", "state", state)
    zipcode = address[3]
    cf_info.set("bill_address", "postalcode", zipcode)
    cardinfo = generate_card()
    phonenumber = cardinfo[0]
    cf_info.set("bill_address", "phone", phonenumber)
    cf_info.add_section("cardinfo")
    cardnumber = cardinfo[1]
    cf_info.set("cardinfo", "cardnumber", cardnumber)
    validmonth = cardinfo[2].split('/')[0]
    cf_info.set("cardinfo", "month", validmonth)
    validyear = cardinfo[2].split('/')[1]
    cf_info.set("cardinfo", "year", validyear)

    cf_info.write(open('info.txt', 'w'))
    print(("* 随机生成身份资料。。。"), flush=True)

# def window_capture(dpath):
#   '''''
# 截屏函数,调用方法window_capture('d:\\') ,参数为指定保存的目录
# 返回图片文件名,文件名格式:日期.jpg 如:2009328224853.jpg
#   '''
#   hwnd = 0
#   hwndDC = win32gui.GetWindowDC(hwnd)
#   mfcDC=win32ui.CreateDCFromHandle(hwndDC)
#   saveDC=mfcDC.CreateCompatibleDC()
#   saveBitMap = win32ui.CreateBitmap()
#   MoniterDev=win32api.EnumDisplayMonitors(None,None)
#   w = MoniterDev[0][2][2]
#   h = MoniterDev[0][2][3]
#   #print w,h　　　#图片大小
#   saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
#   saveDC.SelectObject(saveBitMap)
#   saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
#   cc=time.gmtime()
#   bmpname=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.bmp'
#   saveBitMap.SaveBitmapFile(saveDC, bmpname)
#   Image.open(bmpname).save(bmpname[:-4]+".jpg")
#   os.remove(bmpname)
#   jpgname=bmpname[:-4]+'.jpg'
#   djpgname=dpath+jpgname
#   copy_command = "move %s %s" % (jpgname, djpgname)
#   os.popen(copy_command)
#   return bmpname[:-4]+'.jpg'

def window_capture(filename):
  hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 获取监控器信息
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  w = MoniterDev[0][2][2]
  h = MoniterDev[0][2][3]
  # print w,h　　　#图片大小
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)
  # 截取从左上角（0，0）长宽为（w，h）的图片
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  cc = time.gmtime()
  bmpname = str(cc[0]) + str(cc[1]) + str(cc[2]) + str(cc[3] + 8) + str(cc[4]) + str(cc[5]) + '.bmp'
  tmpname = filename + "-" + bmpname
  saveBitMap.SaveBitmapFile(saveDC, tmpname)

def customized_broswer():
    option = webdriver.ChromeOptions()
    index = random.randint(0, (len(useragentlist) - 1))
    useragent = "--user-agent=" + useragentlist[index]
    option.add_argument(useragent)
    driver =  webdriver.Chrome(chrome_options=option)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    return driver

class Administrator():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read("_task.txt")

    def get_tasks(self):
        return self.cf.sections()

    def get_tasks_len(self):
        return len(self.get_tasks())

    def get_random_task(self):
        return self.get_tasks()[random.randint(0, (self.get_tasks_len() - 1))]

    def is_run_out(self, section):
        count = self.cf.get(section, "count")
        if int(count) <= 0:
            return True
        else:
            return False

    def is_super_link(self, section):
        link = self.cf.get(section, "link")
        if link == "0":
            return True
        else:
            return link

    def is_qa_submit_needed(self, section):
        return self.cf.get(section, "qa_submit")

    def get_qa_content(self, section):
        return self.cf.get(section, "content")

    def is_add_to_card_needed(self, section):
        return self.cf.get(section, "addcart")

    def is_add_wishlist_needed(self, section):
        return self.cf.get(section, "wishlist")

    def get_keyword(self, section):
        return self.cf.get(section, "keyword")

    def is_all_over(self):
        if len(self.cf.sections()) == 0:
            return True
        else:
            return False

    def delete_task(self, section):
        if self.is_run_out(section):
            self.cf.remove_section(section)
            self.cf.write(open('_task.txt', 'w'))
            self.cf.read("_task.txt")

    def finish_task(self, section):
        count = int(self.cf.get(section, "count"))
        count -= 1
        self.cf.set(section, "count", str(count))
        self.cf.write(open('_task.txt', 'w'))
        if count <= 0:
            self.delete_task(section)

if __name__ == "__main__":
    # print(generate_username())
    # print(generate_email())
    # print(generate_password())
    # print(generate_address())
    # print(generate_card())
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    admin = Administrator()
    # if admin.is_all_over() == False:
    #     task = admin.get_random_task()
    #     admin.finish_task(task)
    # else:
    #     print("it is all over...")

    while admin.is_all_over() == False:
        change_proxy()
        generate_info_file()
        task = admin.get_random_task()
        driver = customized_broswer()
        amazonpage = AmazonPage(driver)
        ## registeration
        amazonpage.enter_amazon_page(3000, 5000)
        amazonpage.enter_register_page(3000, 5000)
        registerpage = AmazonRegisterPage(driver)
        registerpage.register(5000, 10000)
        ## add bill address
        amazonpage.enter_account_page(3000, 5000)
        accountpage = AmazonAccountPage(driver)
        accountpage.enter_address_page(3000, 5000)
        addresspage = AmazonAddressPage(driver)
        addresspage.add_address("bill", 5000, 10000)
        ## add payment
        amazonpage.enter_account_page(3000, 5000)
        accountpage = AmazonAccountPage(driver)
        accountpage.enter_payment_page(3000, 5000)
        paymentpage = AmazonPaymentPage(driver)
        paymentpage.add_new_payment(5000, 10000)

        searchpage = AmazonSearchPage(driver)
        searchpage_handle = 0
        asinresult = False
        entry_type = ""
        link = admin.is_super_link(task)
        if link != "0":
            print(("* 开始通过超链接访问产品页。。。"), flush=True)
            amazonpage.enter_super_link(link, 3000, 5000)
            searchpage_handle = amazonpage.get_currenthandle()
            asinresult = True
        else:
            keyword = admin.get_keyword(task)
            print(("* 开始搜索关键词。。。"), flush=True)
            amazonpage.search_asin(keyword, 5000, 8000)
            searchpage_handle = amazonpage.get_currenthandle()

            asinresult = searchpage.find_target_product(task, "normal", int(5))

        if asinresult != False:
            print(("* 开始随意浏览产品页。。。"), flush=True)
            #amazonpage.random_walk(random.randint(35, 50))
            time.sleep(random.randint(60, 120))
            asinpage = AmazonAsinPage(driver)
            searchpage.switch_to_new_page(searchpage_handle)  # 切换到产品页handle

            qa_submit = admin.is_qa_submit_needed(task)
            if qa_submit == "1":
                print(("* 开始提交QA。。。。"), flush=True)
                content = admin.get_qa_content(task)
                asinpage.ask_qa(content, 3000, 5000)
                amazonpage.navigation_back(3000, 5000)
                window_capture("qa")

            wishlist = admin.is_add_wishlist_needed(task)
            if wishlist == "1":
                print(("* 开始添加wishlist。。。。"), flush=True)
                asinpage.add_wishlist(5000, 8000)
                window_capture("addwishlist")

            addcart = admin.is_add_to_card_needed(task)
            if addcart == "1":
                print(("* 开始加购物车。。。"), flush=True)
                asinpage.add_cart(3000, 5000)
                window_capture("addcart")

            searchpage.back_prev_page_by_country(searchpage_handle, 3000, 5000)

            admin.finish_task(task)
        else:
            print(("找不到产品！！！！"), flush=True)

            time.sleep(random.randint(60*5, 120*5))
