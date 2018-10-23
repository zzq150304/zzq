# import requests
# """查看该类的一些基本的 介绍 和 方法"""
# help(requests)
import requests
import json

URL = "https://api.github.com"

def build_url(endpoint):
    return '/'.join([URL,endpoint])     # 主要作用是拼接接口请求地址

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)      # 采用json里提供的第4 种输出格式打印出来，格式更好看

def json_method():
    response = requests.patch(build_url('user'),auth=('1181105615@qq.com','zzq.150304'),json={'company':'haotest',
                                                                                              'email':'1181105615@qq.com'})
    print(better_output(response.text))


if __name__ == '__main':
    json_method()