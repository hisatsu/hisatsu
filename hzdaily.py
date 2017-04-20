#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, urllib, datetime, csv
from urllib import request
from urllib import error
# 1.todo 考虑网络出错时的处理 2.结果存入excel|mysql

# config
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
}
# 匹配一手房数据
pattern1 = re.compile(r'全市签约.*其中住宅(\d+)套')
# match old house data
pattern2 = re.compile(r'摘要.*其中住宅签约(\d+)套')
# get data from webpage and return NUM

# strftime format time
delta = datetime.timedelta(days=1)
start_date = datetime.date(2017, 4, 15)
# start = str(start_date.strftime('%Y%m%d'))
end_date = datetime.date.today() # - delta
# end = str(end_date.strftime('%Y%m%d'))





def gather(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Download Error!', e.reason)
        response = None
    return response

def numbers(response, pattern):
    data = response.read().decode('utf-8')
    return pattern.search(data).group(1)

# 获取两个日期之间的日期 并由此拼出url 获取数据
while start_date < end_date:
    # start 数据需要刷新
    date = start_date.strftime('%Y%m%d')
    url_xf = 'http://www.tmsf.com/upload/report/mrhqbb/' + date + '/xf.html'
    url_esf = 'http://www.tmsf.com/upload/report/mrhqbb/' + date + '/esf.html'
    xfdata = gather(url_xf)
    xf = numbers(xfdata, pattern1)
    print(xf)
    # print(date + '新房:' + gather(url_xf, pattern1))
    esfdata = gather(url_esf)
    esf = numbers(esfdata, pattern2)
    print(esf)
    # print(date + '二手:' + gather(url_esf, pattern2))
    start_date += delta




# class HzdailyCallback:
#     def __init__(self):
#         self.writer = csv.writer(open('hzdaily.csv', 'w'))
#         self.fields = ('date', 'xf', 'esf')
#         self.writer.writerow(self.fields)
#
#     def __call__(self, ):
