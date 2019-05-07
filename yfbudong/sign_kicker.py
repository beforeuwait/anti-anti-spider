# coding=utf-8

"""
    加密方式:
        将参数进行某种排序后，然后md5加密
    属于比较简单的类型
"""

import hashlib


def sign_kicker(city_id, page_id):
    params = {
        'city_id': city_id,
        'page_id': page_id,
        'page_size': '10',
        'selectZoneItems': '',
        'type_id': '1'
    }
    ctx = ''
    for key, value in params.items():
        ctx += '{0}-{1}:{2}-{3}'.format(len(key), key, len(value), value) + ';'
    ctx = ctx.lower() + 'seatune:oAyHBnoWGvualtbJgC0v5QMwwKLk9G0B'
    # md5加密
    m = hashlib.md5()
    b = ctx.encode()
    m.update(b)
    str_md5 = m.hexdigest()
    params.update({'sign': str_md5})
    return params

"""

验证部分
"""
import requests

url1 = 'http://116.62.240.91:3000/zone/infos'
url2 = 'http://116.62.240.91:3000/house/lists'
headers = {
    'Host':	'116.62.240.91:3000',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'http://www.yfbudong.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Referer': 'http://www.yfbudong.com/p_index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive'
}

params = sign_kicker('1036', '3')

rep = requests.get(url2, headers=headers, params=params)
print(rep.url)
print(rep.status_code)
print(rep.content.decode('utf-8'))