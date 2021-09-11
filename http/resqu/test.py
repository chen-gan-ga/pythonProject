import json  # 标准库 内置的 官方提供的不需要下载的

"""
json_str - > python object  json反序列化

python object - > json_str   json序列化

"""

json_str = '''{
    "name": "Felix",
    "age": 18,
    "hobby": ["运动","妹子"],
    "friends": [
        {
            "name": "刘德华"
        },
        {
            "name": "梁朝伟"
        }
    ]
}
'''

print(type(json_str))

# 看看Felix的爱好
python_obj = json.loads(json_str)
print(python_obj, type(python_obj))
#
# # python对象序列化json字符串
dumps_str = json.dumps(python_obj)
print(dumps_str, type(dumps_str))