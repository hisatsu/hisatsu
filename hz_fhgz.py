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
driver.set_window_size(1024, 768)
driver.set_window_position(-2000, 0)
driver.find_element_by_name("username").send_keys(u'粪海孤舟')
driver.find_element_by_name("password").send_keys(u'1q2w3e4r5t')
driver.find_element_by_name("submit").click()
# driver.find_element_by_class_name("grey").click()
time.sleep(random.uniform(1, 2))
# get personal page(mobiel = no), target uid
# settings
pid = '48214539'
uid = '5310405'
reply = [u'另外说一句，快来接我的老破小吧，一家老小急等着钱造瘘啊',
         u'另外说一句，接了我的盘吧，为了还房贷，已经吃了1年翔了啊',
         u'哆啰啰，哆啰啰，站岗冻死我，谁来接破窝……',
         u'另外说一句，接了我的盘，我就不用来口水，上串下跳的托市了啊',
         u'另外说一句，各位父老乡亲，小子在这里说的口感舌燥，还不是为了我那个破盘吗',
         u'另外说一句，我来这里也喊了几个月了，虽然还没人接我的盘，但万一有人傻呢'
        ]

while True:
    try:
        # check notice
        driver.get('http://zzhzbbs.zjol.com.cn/home.php?mod=space&do=notice&view=system&mobile=no')
        time.sleep(1)
        driver.get('http://zzhzbbs.zjol.com.cn/home.php?mod=space&do=notice&view=mypost&mobile=no')
        time.sleep(1)
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




