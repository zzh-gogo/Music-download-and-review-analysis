import json
import execjs
import requests
URL = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

code = ""
with open("code.js", "r+") as r:
    code = r.read()

comments = []

fun = execjs.compile(code)
# res = fun.call(
#     'get', '{"rid":"R_SO_4_1806053199","threadId":"R_SO_4_1806053199","pageSize":"300","orderType":"1","csrf_token":""}')
res = fun.call(
    'get',
    '{"rid":"R_SO_4_1824045033","threadId":"R_SO_4_1824045033","pageNo":"8","pageSize":"1000","cursor":"1657173467035","offset":"0","orderType":"1","csrf_token":""}')

response = requests.post(url=URL, params=res)
response = response.json()
count = 1
for i in response["data"]["comments"]:
    print(count, i["content"])
    count += 1
    comments.append(i["content"])
