import re
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]
aname="a.txt"
bname="b.txt"
cname="c.jpg"
acount=0
bcount=0
ccount=0
for n in urls:
    if re.findall("a.txt",n):
       acount+=1
    elif re.findall("b.txt",n):
        bcount+=1
    elif re.findall("c.jpg",n):
        ccount+=1
print(aname,acount)
print(bname,bcount)
print(cname,ccount)

