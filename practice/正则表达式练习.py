import re
str = "lilei a is GOOD boy also a good student"
#re.I不区分大小写,compile是编译正则表达式
res = re.compile(r'good',re.I)

#match只从字符串开始位置匹配，开头未知没有则匹配不到，search在整个字符串中匹配，有group()方法:
print(res.search(str).group(0))
print(res.findall(str))

#字符串替换，将匹配到的字符替换成hello
print(re.sub(r'a[0-9]b','hello','abca2bb'))

str1 = "www.baidu.com"
#因为.在正则当中表示任意字符，所以需要转意，r是告诉python不要对\.进行转意
print(re.split(r'\.',str1))




