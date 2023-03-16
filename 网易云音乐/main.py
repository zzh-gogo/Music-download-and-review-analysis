import json
import execjs

code = ""
with open("code.js", "r+") as r:
    code = r.read()

fun = execjs.compile(code)
res = fun.eval("get()")
print(res)
