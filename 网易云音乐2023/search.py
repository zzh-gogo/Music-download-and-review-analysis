import requests
import execjs
import re
url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token=2b6e17f59d6a50fb6fb367808ada8e8a'
headers = {
'cookie': '_ntes_nnid=dadfdff49eb3abb3f601a188b041e01f,1678256447403; _ntes_nuid=dadfdff49eb3abb3f601a188b041e01f; NMTID=00OPQXshDbPWJ6Wpka8pfZUYborYOsAAAGGv-EhMQ; WEVNSM=1.0.0; WNMCID=shjsqb.1678256448043.01.0; WM_TID=Vx6Mk%2BMZwJBFBVRFEAeVUuYJE%2F7Xwzuo; WM_NI=kHqNd9IqqBXJS0Or1shLL1VOBI%2Fi61Whf18mXzq%2FtX%2B43uAfM4C5R2BPMqAFYtd1lrXG3q%2BtIBl5Gc6REsuxYrYn1pD2vrmTJZYy8beiM5IsCSgErS4OfA0mZGCVvL1LckQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea7dc6a9b8c82adcf3ced928aa6c15a869f8f82d86e9098e58dc441af9e8da5f92af0fea7c3b92aa998bfafe7338bafbfa3db4291f08193b479ac9484d2d5458297e18ab53b95b8aad2bb679ca6bfd0f754e9ecfd96c46e8fec8dd6d13a82908392c44e9bacacd2ef7a9c99fd92aa808b9ea4d6c669f68e8b94f8749bae978fb47c88eeba93f0608a86979abb6aa7b783d6cc79818da9a6f159f891aaa2b3679a998db7f548f394ad8cd437e2a3; __snaker__id=pzEBA2cYWXlsx4bV; YD00000558929251%3AWM_NI=mXiMUEhlJlFJRC%2FzrvTUjDfxPuonND%2BouH%2FdCx08kCG1ZAx9%2BN1JaDljERgmSwdgTDpwwKi%2FVISZ%2FrmDGzxc2rDwZcwm3pS7K7Q652fCZcfHmPtKx%2FY9RBQ88eCmdHMwZzk%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee9ac23bf693e1d6fb7fbcac8fb3c15f828a9a86c46f8d88bf89b37e94ac8294f12af0fea7c3b92aaf88a7aed84facb4868dc542929de19bf17e988ba6a5e57494aba18fcd50e9b1bba9ae7081a800d9ea4985ef96a2fb33e992ffabe450b0b68bb3e66791a9ac88d750b4a9b9acec2596979dbbae7aaf9c899bfb69f2ae8c98d969b5b3fd91d23d89e99fd7b83aa69d9684e544af90bcacfb259be79ea3d434fcbb8d8ee7448fa9969bea37e2a3; YD00000558929251%3AWM_TID=nEqHakk03EFEQEQEEVLBKPH7xwvatIp7; gdxidpyhxdE=2ihAKxYzr1q6syls5%2Fwwmjx4ZOqi4UQyV11BCiqYzWDoQPBWpOgJ6U%2Bb%2FuE8v29i%5CoQign5%5C2fiBu24%2FKA1QhBSMAy44I2klh3ZHocZWVLIGUxbYV6QLpehICW8bV5tY6UY3PS8yciEZEtRkZrzkL8O9Hsd4jkczP1vg%5C9xo4AUdMzan%3A1678521878830; MUSIC_U=a030e92c2e6047008fb2672331bd265e694c3f9b6b66d1d9ab21125a180326a2993166e004087dd332ac5d5d84d5b6e18958faa7bcf9d86354f9f6a1d0d3a1cd3e3910f24ae5c308a0d2166338885bd7; __csrf=2b6e17f59d6a50fb6fb367808ada8e8a; ntes_kaola_ad=1; playerid=18502136; JSESSIONID-WYYY=2GVAtCJ0rImUX42QgIaByc0%2FBmrch%5ChzIFKexeSAKE05gu3dn09cqPG0Arc%2BBiCN1bCr9Y00dDZ%2FVHur0g1vlsHRRDS33%2Fd%2B5E2%5CawFrJft4MzrxNIWwAx78d6YNRH2xHSTgZ5x7tR8uAEMK6tVSFAKqEhhr2dDAKx0l8sNdY1SoiY8p%3A1678539986019; _iuqxldmzr_=33',
'origin': 'https://music.163.com',
'referer': 'https://music.163.com/search/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
data = {
    'params': 'fhlUz8UcDKTkoTXnbBx511JHBmO/m6BSX247cP8N95JSZ+65x8HYEtF/h/iqVTL71MnBvbEdc8CrPT9iK0BIc7GTCFPjzfR+dyFHZ7mSmtsEJmfW+jUVLHRQnTL+3YMrlgd1rXtXFOP5vYO07YDrxowR3nDQ2dDB44uA7gokeYKYHnatXTgpcuX8NwL5RcsDgH29dDsT3DP62FwRMYQ8QKLMuugazvt6Rg1mfqlr1Oo7s40bH0yaw53cSpIweSAr9sAO8whDBcS3v16FnlobHSY3mpHpzWgMIcziWpateBYXFsQOnMG4QHb8KhlxLmQJ',
    'encSecKey': 'b202ebe98eff987eda66d1d65dd63b9a650f2fca205fc82f65b11aa6e6e2463b4a73f50014f1eaa79af3385eeb917f97cdd74f2cb9748a8a78ff4206b5a3fa1261736ea7b045501c0daa9c253a70d00d5b1fa4789416b6056b643633a7f19a5dd63505cb67cc55138cd489d9a3265af07125ec9fb4f61a8512f79af97a6d16b5'
}
resp = requests.post(url=url,headers = headers,data=data)
print(resp.json())
json_data=resp.json()
songs = json_data['result']['songs']
for song in songs:
    name = song['name']
    id = song['id']
    print(id,name)