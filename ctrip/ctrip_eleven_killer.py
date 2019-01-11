# coding=utf-8

"""
    autohr: wangjiawei
    date: 2019-01-11

    解决携程加密的 callback和 eleven

    callback是通过一段js随机生产，长度 15位
    eleven 目前携程是有好几套加密算法生产
            因此在解析函数里会出现whle 是因为并不能每种加密都解密

    测试的时候用的酒店的评论
    目前是ok的

"""

import re
import time
import requests
import execjs


headers_ocean = {
    'host': 'hotels.ctrip.com',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'referer': 'https://hotels.ctrip.com/hotel/438080.html',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


headers_cmt = {
    'host': 'hotels.ctrip.com',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'if-modified-since': 'Thu, 01 Jan 1970 00:00:00 GMT',
    'referer': 'https://hotels.ctrip.com/hotel/438080.html',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_callback():
    """拿到callback，算出来的一个随机15位字符串"""
    callback = """
        var callback = function() {
        for (var t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], o = "CAS", n = 0; n < 15; n++) {
            var i = Math.ceil(51 * Math.random());
            o += t[i]
        }
        return o
        };
            """
    js = execjs.compile(callback)
    return js.call('callback')


def deal_ocean(js_txt, hotel_id, call_back):
    """处理js_txt"""
    # 第一步先还原
    js_txt = re.sub('eval', 'return', js_txt)
    js_1 = execjs.compile(js_txt)
    ocean_txt = js_1.call('f')

    # 第二部开始处理这段js,要在execjs里执行，需要添加一些头
    # 先补充变量,需要知道hotel_id

    variable = """
            var hotel_id = "%s";
            var site = {};
            site.getUserAgent = function(){};
            var Image = function(){};
            var window = {};
            window.document = {body:{innerHTML:"1"}, documentElement:{attributes:{webdriver:"1"}}, createElement:function(x){return {innerHTML:"1"}}};
            var document = window.document;
            window.navigator = {"appCodeName":"Mozilla", "appName":"Netscape", "language":"zh-CN", "platform":"Win"};
            window.navigator.userAgent = site.getUserAgent();
            var navigator = window.navigator;
            window.location = {};
            window.location.href = "http://hotels.ctrip.com/hotel/%s.html";
            var location = window.location;
            var navigator = {userAgent:{indexOf: function(x){return "1"}}, geolocation:"1"};
            """% (hotel_id, hotel_id)

    # 第三步开始改造js
    js_final = ''
    js_final += variable
    ocean_txt = re.sub(';!function', 'function get_eleven', ocean_txt)
    js_final += ocean_txt[:-3]
    rep_cnt = re.findall('{0}.*?";\'\)\)'.format(call_back), js_final, re.S)[0]
    eleven = rep_cnt.split('+')[1]
    # 然后替换
    js_final = js_final.replace(rep_cnt, 'return{0}'.format(eleven))
    # 找到嘲讽那段，然后替换
    sneer = re.findall(' \[32769,26495,32473.*,49,51,107,21734]\*/', js_final, re.S)[0]
    js_final = js_final.replace(sneer, '=1);')
    # 第四部，执行
    js_content = execjs.compile(js_final)
    return js_content.call('get_eleven')


def main_logic(hotel_id):
    # 1. 拿到callback和时间戳请求ocean.js
    while True:
        try:
            print('重试.....')
            call_back = get_callback()
            t = int(time.time()*1000)
            ocean_js = request_oceanball(call_back, t)
            # 接下来处理ocean_js
            eleven = deal_ocean(ocean_js, hotel_id, call_back)
            break
        except Exception as e:
            print(e)
    # 拿到eleven时候再去请求评论
    get_comment(eleven, hotel_id)


def request_oceanball(cb, t):
    url_ocean = 'https://hotels.ctrip.com/domestic/cas/oceanball?callback={0}&_={1}'.format(cb, t)
    html = requests.get(url_ocean, headers=headers_ocean)
    return html.content.decode('utf-8')


def get_comment(eleven, hotel_id):
    url = 'https://hotels.ctrip.com/Domestic/tool/AjaxHotelCommentList.aspx'
    params = {
        'MasterHotelID': hotel_id,
        'hotel': hotel_id,
        'NewOpenCount': '0',
        'AutoExpiredCount': '0',
        'RecordCount': '6708',
        'OpenDate': '2012-01-01',
        'card': '-1',
        'property': '-1',
        'userType': '-1',
        'productcode': '',
        'keyword': '',
        'roomName': '',
        'orderBy': '2',
        'currentPage': '3',
        'viewVersion': 'c',
        'contyped': '0',
        'eleven': eleven,
        'callback': get_callback(),
        '_': int(time.time()*1000)}
    html = requests.get(url, headers=headers_cmt, params=params)
    print(html.status_code)
    print(html.content.decode('utf-8'))


if __name__ == '__main__':
    main_logic('438080')