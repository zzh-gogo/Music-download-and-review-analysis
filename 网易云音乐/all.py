import matplotlib.pyplot as plt
from snownlp import SnowNLP
import json
import execjs
import requests
URL = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

code = ""
with open("code.js", "r+") as r:
    code = r.read()

comments = []

fun = execjs.compile(code)
res = fun.call(
    'get', '{"rid":"R_SO_4_1954694243","threadId":"R_SO_4_1954694243","pageSize":"300","orderType":"1","csrf_token":""}')
print(res)
response = requests.post(url=URL, params=res)
response = response.json()
count = 1
for i in response["data"]["comments"]:
    print(count, i["content"])  
    count += 1
    comments.append(i["content"])


stat = []
for i in range(0, 10):
    stat.append(0)
print(stat)

for i in comments:
    temp = SnowNLP(i)
    score = temp.sentiments
    print(score)
    score = int(score*10)
    stat[score] += 1

plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], stat)
plt.show()
