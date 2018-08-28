#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import os
import sys
import win32api
import win32con
import pyautogui
from win32api import GetSystemMetrics
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver
        self.screen_width = GetSystemMetrics(0)
        self.screen_heigth = GetSystemMetrics(1)

    def log_location(self):
        print(sys._getframe().f_code.co_filename + " : " + sys._getframe().f_code.co_name + " : " + sys._getframe().f_lineno)

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, content, *locator):
        try:
            time.sleep(random.randint(3, 6))
            # browser.execute_script('window.stop()')
            input_box = self.driver.find_element(*locator)
        except Exception as e:
            print(type(e))
        else:
            if input_box.is_displayed():
                self.driver.set_page_load_timeout(1)
                self.driver.set_script_timeout(1)
                for character in content:
                    try:
                        input_box.send_keys(character)
                        time.sleep(random.randint(300, 800) / 1000)  # pause for 0.3 seconds
                    except Exception as e:
                        print(type(e))
                        try:
                            input_box.send_keys(character)
                            time.sleep(random.randint(300, 800) / 1000)  # pause for 0.3 seconds
                        except Exception as e:
                            print(type(e))
                            pass
                        finally:
                            pass
                self.driver.set_page_load_timeout(30)
                self.driver.set_script_timeout(30)

    def random_sleep(self, begin, end):
        time.sleep(random.randint(begin, end) / 1000)

    def mouse_move(self, x, y):
        move_time = random.randint(100, 1500) / 1000
        pyautogui.moveTo(x, y, move_time)

    def random_mouse_move(self, count):
        move_count = 0
        while move_count < count:
            x = random.randint(0, int(self.screen_width / 3))
            y = random.randint(0, int(self.screen_heigth / 3)) + 200
            move_time = random.randint(1, 20) * 1000 / 10000
            pyautogui.moveTo(x, y, move_time)
            time.sleep(random.randint(2, 4))
            move_count += 1

    def mouse_scoll(self, distance, direction):
        move_count = 0
        while move_count < distance:
            scroll_count = random.randint(300, 800)
            for i in range(scroll_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, direction)
            time.sleep(random.randint(1, 3))
            move_count += 1

    def enter_back(self):
        return

    def page_reload(self):
        return

    def scoll_to_top(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execut_script(js)