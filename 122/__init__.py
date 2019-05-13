# coding=utf-8

"""
    重点违章

    update:
        2019-05-13: 进入四川官网，发现出现带计算的验证码
        分析js发现，请求里有token字段，仅仅是没有启用而已
        cookie 里的 tmri_csfr_token 也是由主页写入的
        然后发现 accessToken是由主页颁发
        !! 以上仍然不行
        这下录入 checkType试试
        !! 成功
        牛皮， checkType 竟然是写死的


"""