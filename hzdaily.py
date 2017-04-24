#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import urllib
import datetime
import pymysql
from urllib import request
from urllib import error


start_date = datetime.date(2016, 1, 1)
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='1q2w3e', db='mysql', charset='utf8' )
cur = conn.cursor()
cur.execute("USE djcode")

def getPages(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '}
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Download Error!', e.reason)
        response = None
    return response

def getData(response, pattern):
    data = response.read().decode('utf-8')
    return pattern.search(data).group(1)

def store(date, xf, esf):
    cur.execute("INSERT INTO hzDaily (date, xf, esf) VALUES (%s, %s, %s)", (date, xf, esf))
    cur.connection.commit()

try:
    end_date = datetime.date.today()
    delta = datetime.timedelta(days=1)
    pattern1 = re.compile(r'全市签约.*其中住宅(\d+)套')
    pattern2 = re.compile(r'摘要.*其中住宅签约(\d+)套')
    while start_date < end_date:
        date = start_date.strftime('%Y%m%d')
        url_xf = 'http://www.tmsf.com/upload/report/mrhqbb/' + date + '/xf.html'
        # print(url_xf)
        url_esf = 'http://www.tmsf.com/upload/report/mrhqbb/' + date + '/esf.html'
        # print(url_esf)
        xfdata = getPages(url_xf)
        esfdata = getPages(url_esf)
        xf = getData(xfdata, pattern1)
        esf = getData(esfdata, pattern2)
        store(date, xf, esf)
        print(date + 'done!')
        start_date += delta
finally:
    cur.close()
    conn.close()

