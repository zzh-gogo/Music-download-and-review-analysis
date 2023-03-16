import execjs
import requests

URL = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="

code = ""
with open("code.js", "r") as r:
    code = r.read()
# print(code)


fun = execjs.compile(code)
res = fun.eval("get('1824045033')")
print(res)


response = requests.post(url=URL, params=res)

print(response.text)

data = response.json()

music_url = data["data"][0]["url"]

print(music_url)

response = requests.get(music_url)

with open("music.m4a", "wb") as w:
    w.write(response.content)