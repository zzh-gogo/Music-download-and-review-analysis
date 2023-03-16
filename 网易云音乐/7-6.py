import execjs

code = ""
with open("7-6.js", "r") as r:
    code = r.read()
# print(code)


fun = execjs.compile(code)

res = fun.eval("get('1901371647')")
print(res)

