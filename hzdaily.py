# -*- coding: utf-8 -*-
import re, urllib, datetime
from urllib import request
# 1.todo 考虑网络出错时的处理 2.结果存入excel|mysql
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
}
# 匹配一手房数据
pattern1 = re.compile(r'全市签约.*其中住宅(\d+)套')
# match old house data
pattern2 = re.compile(r'摘要.*其中住宅签约(\d+)套')
# get data from webpage and return NUM
def gather(pattern):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return pattern.search(data).group(1)



# strftime format time
delta = datetime.timedelta(days=1)
start_date = datetime.date(2017, 2, 1)
# start = str(start_date.strftime('%Y%m%d'))
end_date = datetime.date.today() - delta
# end = str(end_date.strftime('%Y%m%d'))
# 获取两个日期之间的日期 并由此拼出url 获取数据
while start_date < end_date:
    # start 数据需要刷新
    start = str(start_date.strftime('%Y%m%d'))
    url = 'http://www.tmsf.com/upload/report/mrhqbb/' + start + '/xf.html'
    print(start + '新房:' + gather(pattern1))
    url = 'http://www.tmsf.com/upload/report/mrhqbb/' + start + '/esf.html'
    print(start + '二手:' + gather(pattern2))
    start_date += delta


print('done.')