#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/22 20:49

import requests

# 发送参数
# 1. url参数  url后 ?key=value 也叫查询参数 params
# 什么请求方法都可以携带
# url最长1024字节，数据量有限，在地址栏可见
# 测试接口，返回json数据
# url = 'http://httpbin.org/get'
# # ?page=2&sex=1
params = {'page': 2, 'sex': 1}
# 方法的 params参数
# res = requests.get(url=url, params=params)
# print(res.text)

# 2. 表单参数  html form表单，有可能需要设置 content-type: application/x-www-form-urlencoded; charset=UTF-8
# post put patch
# url = 'http://httpbin.org/post'
# data = {'username': '心蓝', 'pwd': '123456'}
# 方法的data参数
# res = requests.post(url=url, params=params, data=data)
# print(res.text)
# requests.put
# requests.patch
# requests.delete

# 3. json数据
# post put patch
url = 'http://httpbin.org/put'
data = {'username': '心蓝', 'pwd': '123456'}
# 方法的json参数
# res = requests.put(url=url, json=data)
# print(res.text)

# 4. 请求头 headers
url = 'http://httpbin.org/post'
headers = {
    'X-Lemonban-Media-Type': 'lemonban.v1'
}
# headers参数传递请求头
# res = requests.post(url=url, data=data, headers=headers)
# print(res.text)

# 5. cookies
cookies = {'times': '1'}
# cookies参数传递cookie
res = requests.post(url=url, data=data, cookies=cookies)
print(res.text)