#author:xm
#coding:utf-8

import pymysql

# 创建连接
conn = pymysql.connect(host='58.206.97.104', port=3306, user='root', passwd='Xt2018', db='my_test')
# 创建游标
cur = conn.cursor()
#学生列表
data = [
    (3,"wangwu",21,"M"),
    (4,"maliu",20,"F")
]

# 执行SQL，并返回收影响行数
#result = cur.executemany("insert into students VALUES (%s,%s,%s,%s) ",data)
result1 = cur.execute("select * from students")

conn.commit()

print(cur.fetchone())
print(cur.fetchmany(2))
print(cur.fetchall())
conn.close()


