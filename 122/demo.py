# coding=utf-8

"""
测试文件

"""


import requests
import time


headers_home = {
    'Host': 'sc.122.gov.cn',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://sc.122.gov.cn/views/swfzpub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

url_a = 'https://sc.122.gov.cn'

url_home = 'https://sc.122.gov.cn/views/viopub.html'

# 测试
# 拿到jsessionid和tmrl_csfr_token后 请求验证码做验证

session = requests.session()
rep0 = session.get(url_a, headers=headers_home, timeout=15, verify=False)
print(rep0.status_code)
print(rep0.cookies.items())
time.sleep(1)
rep = session.get(url_home, headers=headers_home, timeout=15, verify=False)
session.cookies.update({'qt': '664341', '_uab_collina': '155771222671336064679181'})

# 请求 checkType
url_check = 'https://sc.122.gov.cn/m/tmri/captcha/checkType'
headers_check = {
    'Host': 'sc.122.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://sc.122.gov.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://sc.122.gov.cn/views/swfzpub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}
payloads_c = {'checktype': 'YhIXAvDLcynICIFh'}
repc = session.post(url_check, headers=headers_check, data=payloads_c, timeout=15, verify=False)
print(repc.status_code)
print(repc.content.decode('utf-8'))
time.sleep(1)
# 请求验证码
print(session.cookies.items())

url_c = 'https://sc.122.gov.cn/m/tmri/captcha/math?nocache={0}'

header_c = {
    'Host': 'sc.122.gov.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://sc.122.gov.cn/views/viopub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}
time.sleep(2)
rep2 = session.get(url_c.format(int(time.time()*1000)), headers=header_c, timeout=30, verify=False)
with open('captcha.png', 'wb') as f:
    f.write(rep2.content)

# 请求数据

url_d = 'https://sc.122.gov.cn/m/viopub/getVioPubList'

headers = {
    'Host': 'sc.122.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '62',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://sc.122.gov.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://sc.122.gov.cn/views/mfjjpub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',

}

payloads = {
    'page': '1',
    'size': '20',
    'startTime': '2019-04-13',
    'endTime': '2019-05-13',
    'gsyw': '01'
}

token = input('请输入结果:\t')

payloads.update({'csessionid': token})

rep3 = session.post(url_d, headers=headers, data=payloads, timeout=15, verify=False)
print(session.cookies.items())
print(rep3.status_code)
print(rep3.content.decode('utf-8'))
