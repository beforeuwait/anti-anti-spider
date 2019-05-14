# coding=utf-8

"""
用来测试当前的采集思路在各个省份是否可行
"""
import requests
import time

session = requests.session()


headers_home = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://sc.122.gov.cn/views/swfzpub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

headers_check = {
    'Host': 'cq.122.gov.cn',
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

headers_captcha = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://cq.122.gov.cn/views/viopub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

headers = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '62',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://cq.122.gov.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://cq.122.gov.cn/views/mfjjpub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',

}


def request_home_page(code):
    url_home = 'https://{0}.122.gov.cn'.format(code)
    headers_home.update({'Host': '{0}.122.gov.cn'.format(code)})
    rep0 = session.get(url_home, headers=headers_home, timeout=15, verify=False)
    print('请求主页:\t', rep0.status_code)
    print('主页获取cookie:\t', rep0.cookies.items())


def request_main_page(code):
    url_main = 'https://{0}.122.gov.cn/views/viopub.html'.format(code)
    headers_home.update({'Host': '{0}.122.gov.cn'.format(code)})
    rep = session.get(url_main, headers=headers_home, timeout=15, verify=False)
    session.cookies.update({'qt': '664341', '_uab_collina': '155771222671336064679181'})
    print('目标页面:\t', rep.status_code)
    print('目标页面更新后的cookie:\t', session.cookies.items())


def request_check_type(code):
    url_check = 'https://{0}.122.gov.cn/m/tmri/captcha/checkType'.format(code)
    headers_check.update({'Host': '{0}.122.gov.cn'.format(code)})
    payloads_c = {'checktype': 'YhIXAvDLcynICIFh'}
    repc = session.post(url_check, headers=headers_check, data=payloads_c, timeout=15, verify=False)
    print('请求check type:\t', repc.status_code)
    print('返回内容:\t', repc.content.decode('utf-8'))


def request_captcha(code):
    url_c = 'https://{0}.122.gov.cn/m/tmri/captcha/math?nocache={1}'.format(code, int(time.time()*1000))
    headers_captcha.update({'Host': '{0}.122.gov.cn'.format(code)})
    rep2 = session.get(url_c.format(int(time.time() * 1000)), headers=headers_captcha, timeout=30, verify=False)
    with open('captcha.png', 'wb') as f:
        f.write(rep2.content)
    print('验证码已保存')


def requests_data(code):
    url_d = 'https://{0}.122.gov.cn/m/viopub/getVioPubList'.format(code)
    headers.update({'Host': '{0}.122.gov.cn'.format(code)})
    payloads = {
        'page': '1',
        'size': '20',
        'startTime': '2019-05-12',
        'endTime': '2019-05-13',
        'gsyw': '01'
    }
    token = input('请输入结果:\t')

    payloads.update({'csessionid': token})

    rep3 = session.post(url_d, headers=headers, data=payloads, timeout=15, verify=False)
    print('当前cookie:\t', session.cookies.items())
    print('请求数据:\t', rep3.status_code)
    print('接口内容:\t', rep3.content.decode('utf-8'))


def main(code):
    # 请求主页
    request_home_page(code)
    time.sleep(1)
    request_main_page(code)
    time.sleep(1)
    request_check_type(code)
    time.sleep(1)
    request_captcha(code)
    # 请求数据
    requests_data(code)


if __name__ == '__main__':
    main('bj')