#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
import re
import random


# login
mobile_emulation = {
    "deviceMetrics": {"width": 1024, "height": 768, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
                 "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://zzhzbbs.zjol.com.cn/member.php?mod=logging&action=login&mobile=1")
time.sleep(random.uniform(1, 2))
driver.find_element_by_name("username").send_keys(u't8oo')
driver.find_element_by_name("password").send_keys(u'1q2w3e4r5t')
driver.find_element_by_name("submit").click()
# driver.find_element_by_class_name("grey").click()
time.sleep(random.uniform(1, 2))
# get personal page(mobiel = no), target uid
# settings
pid = '48209419'
uid = '5302519'
reply = [u'这货帽子缀着‘lv’，喜滋滋',
         u'再多回50帖，奖励1个烂虾；多回100帖，奖励1条臭鱼。都可以带回家给你老娘吃',
         u'又牵着你妈出来卖，还不马路上跪着求人接盘去，你那脏病破烂的房子白送也没人要吧，无论行情好坏。',
         u'你智商真的有问题，好好想想。不过估计你也想不通',
         u'5毛钱拿好，回去买顿好的。让你老娘也别再出去卖了。孤儿寡母也是不容易。',
         u'j回家抬头一看，门头上两个大字“翠顶”，不由得心旷神怡，连道“好字，好字！”',
        ]

while True:
    try:
        driver.get(
            "http://zzhzbbs.zjol.com.cn/home.php?mod=space&uid=" + uid + "&do=thread&type=reply&view=me&from=space&mobile=no")

        time.sleep(random.uniform(1, 2))
        handle1 = driver.current_window_handle
        # get the pid of the latest reply
        source = driver.page_source
        pattern1 = re.compile(r'mod=redirect.*pid=(\d{8})')
        pid_latest = pattern1.search(source).group(1)
        print(pid_latest)

        if int(pid_latest) > int(pid):
            # go to the latest reply
            pid = pid_latest
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//table/tbody/tr[3]/td/a')))
            element.click()
            # switch to latest window
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
            # click reply button
            table_id = 'pid' + pid_latest
            xpath_pid = '//*[@id="' + table_id + '"]/tbody/tr[4]/td[2]/div/div/em/a[1]'
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath_pid)))
            element.click()
            # reply it
            # time.sleep(random.uniform(1, 2))
            # switch to the rich text frame
            driver.switch_to.frame('e_iframe')
            driver.find_element_by_xpath("//body[@spellcheck='false']").send_keys(reply[random.randrange(len(reply))])
            driver.switch_to.parent_frame()
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, 'replysubmit')))
            element.click()
            reply_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
            time.sleep(random.uniform(3, 4))
            driver.close()
            driver.switch_to.window(handle1)
            print(pid_latest + 'replyed@' + reply_time)

    except BaseException as e:
        print(e)
        time.sleep(2)

    time.sleep(random.uniform(5, 10))




