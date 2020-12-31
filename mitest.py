#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:50:55 2018

@author: xiaweiyi
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.ui as ui
import datetime
import time

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://www.mi.com/")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("扫码登录").click()
"""
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id("pwd").send_keys("")
driver.find_element_by_id("login-button").click()
name = input("输入验证码：")
driver.find_element_by_id("captcha-code").send_keys(name)
driver.find_element_by_id("login-button").click()

ignr=input("手动点发送短信：")
num = input("输入手机验证码：")
driver.find_element_by_name("ticket").send_keys(num)
driver.find_element_by_link_text("确定").click()

driver.get("https://www.mi.com/seckill/")

#driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/span/ul[0]/li[0]/a/span[1]/span[4]').click()
"""
num = input("登录完了吗")

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        print(now)
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.get("https://www.mi.com/seckill/")
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/ul[1]/li[8]/a/span[2]/span[5]').click()
            break

driver.get("https://www.mi.com/seckill/")
try:
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/ul[1]/li[8]/a/span[2]/span[5]').click()
    print('执行了try')
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_xpath('//li[1]/a'))
    driver.find_element_by_id("J_buyBtnBox").find_element_by_xpath('//li[1]/a').click()

except:
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/span/ul[1]/li[8]/a/span[1]').click()
    print("执行了except")
    # driver.set_window_size(1600,5000)
    # 要等页面加载完
    # WebDriverWait(driver, 2).until(driver.find_element_by_id('J_buyBtnBox'))
    # jsCode = "var q=document.documentElement.scrollTop=600"
    # driver.execute_script(jsCode)
    driver.find_element_by_id("J_buyBtnBox").find_element_by_xpath('//li[1]/a').click()

# buy_on_time('2018-10-26 16:03:50')
print("请继续")