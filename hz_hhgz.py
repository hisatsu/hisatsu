#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
driver.find_element_by_name("username").send_keys(u't800')
driver.find_element_by_name("password").send_keys(u'1q2w3e4r5t')
driver.find_element_by_name("submit").click()
# driver.find_element_by_class_name("grey").click()
time.sleep(random.uniform(1, 2))
# get personal page(mobiel = no), target uid
# settings
pid = '48207330'
uid = '5310405'
reply = [u'好好干。再回100贴明天的盒饭就有着落了。多回50帖，奖励1个烂虾；多回100帖，奖励1条臭鱼。都可以带回家给你老娘吃',
         u'又牵着你妈出来卖，还不马路上跪着求人接盘去，你那脏病破烂的房子白送也没人要吧，无论行情好坏。',
         u'有手有脚的干什么不好，非要出来干这缺德事？5毛钱拿好，回去买顿好的。让你老娘也别再出去卖了。你也是不容易。'
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
            driver.find_element_by_xpath('//table/tbody/tr[3]/td/a').click()
            # switch to latest window
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
            # click reply button
            time.sleep(random.uniform(1, 2))
            table_id = 'pid' + pid_latest
            xpath_pid = '//*[@id="' + table_id + '"]/tbody/tr[4]/td[2]/div/div/em/a[1]'
            driver.find_element_by_xpath(xpath_pid).click()
            # reply it
            time.sleep(random.uniform(1, 2))
            # switch to the rich text frame
            driver.switch_to.frame('e_iframe')
            driver.find_element_by_xpath("//body[@spellcheck='false']").send_keys(reply[random.randrange(len(reply))])
            driver.switch_to.parent_frame()
            driver.find_element_by_name('replysubmit').click()
            reply_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
            time.sleep(random.uniform(1, 2))
            driver.close()
            driver.switch_to.window(handle1)
            print(pid_latest + 'replyed@' + reply_time)
    except BaseException as e:
        print(e)
        time.sleep(2)

    time.sleep(random.uniform(5, 10))




