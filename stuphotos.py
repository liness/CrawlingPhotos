import urllib2

url = 'http://*'
banji = []
zhuanye = []
for a in range(0,10):
    for b in range(1,10):
        banji.append(str(a) + str(b))
for c in range(0,10):
    for d in range(1,3):
        zhuanye.append(str(c) + str(d))

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name

for year in range(11, 15):
    for xh in zhuanye:
        for nj in banji:
            for i in range(1, 40):
                if i < 10:
                    xuehao = str(year) + str(xh) + str(nj) + '0' + str(i)
                    student_url = url + xuehao+'.jpg'
                    print(student_url)
                    try:
                        getFile(student_url)
                    except IOError:
                        pass
                else:
                    xuehao = str(year) + str(xh) + str(nj) + str(i)
                    student_url = url + xuehao+'.jpg'
                    print(student_url)
                    try:
                        getFile(student_url)
                    except IOError:
                        pass

