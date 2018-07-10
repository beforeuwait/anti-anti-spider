# coding=utf8

"""
    date: 2018/07/10
    瓜子的尿性就是，在改变 ua或者ip后，打开页面会先去验证 antipas这个字段，在cookie里

    status_code 出现 203就代表出现js验证

"""

import requests
import os
import re

session = requests.Session()
proxy = {
        # 省略掉
    }

url = "https://www.guazi.com/cd"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Host": "www.guazi.com",
    "Referer": "https://www.guazi.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

session.headers.update(headers)
session.proxies.update(proxy)

# 请求 js
with session.get(url, headers=headers, proxies=proxy) as res:
    print(res.status_code)
    print(res.cookies.items())
    session.cookies.update(res.cookies)

html = res.content.decode('utf8')

js_text = re.findall('<script type="text/javascript">(.*?)</script>', html, re.S)[0].replace("xredirect(name,value,url,'https://')", "console.log(value)")

# 保存js
with open('js.js', 'w', encoding='utf8') as f:
    f.write(js_text)
    f.write('phantom.exit(0)')

# 读取js
path = os.path.abspath('./js.js')
cmd = "phantomjs {0}".format(path)
antipas = os.popen(cmd).read().strip()
session.cookies.update({"antipas": antipas})

print(session.cookies.items())

html = session.get(url, headers=headers, proxies=proxy)

print(html.status_code)
print(html.content.decode('utf8'))