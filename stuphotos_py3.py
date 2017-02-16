#coding:utf8
#使用python3写的爬虫程序
import requests
nianji=[]
banji=[]
xuehao=[]
def getImg(stu_url):
    r = requests.get(stu_url)
    name = stu_url.split('/')[-1]
    html = r.content
    if not r:
        return
    else:
        f = open(name, 'wb')
        c = f.write(html)
        f.close()
        print("OK   !"+name,)

url = 'http://61.181.145.1:88/Stuphotos/'
for a in range(0,10):
    for b in range(1,3):
        nianji.append(str(a)+str(b))
for c in range(0,10):
    for d in range(1,9):
        banji.append(str(c)+str(d))
for e in range(0,4):
    for f in range(1,10):
        xuehao.append(str(e)+str(f))

for g in [14]:
    for h in nianji:
        for i in banji:
            for j in xuehao:
                stu_xh=str(g)+str(h)+str(i)+str(j)+'.jpg'
                stu_url=url+stu_xh
                print(stu_url)
                try:
                    getImg(stu_url)
                except IOError:
                    pass
print("------------100%-----------")
