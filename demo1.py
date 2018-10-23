# import requests
# """查看该类的一些基本的 介绍 和 方法"""
# help(requests)
import requests
import json

URL = "https://api.github.com"

def bulid_url(canshu):
    return "/".join([URL,canshu])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():         # 请求方法
    response=requests.get(bulid_url('users/zzq150304'))
    # print(a.text)
    print(better_output(response.text))

if __name__ == "__main__":
    request_method()
