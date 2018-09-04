#author:xm
#coding:utf-8

import socket
server = socket.socket()
server.bind(('localhost',6369)) #绑定要监听端口
server.listen() #监听
#print("等电话打进来")
conn,addr = server.accept()  # 等电话打进来
# conn就是客户端连过来而在服务器端为其生成的一个连接实例
# print(conn,addr)
# print("电话来了")

data = conn.recv(1024)
print("recv:",data.decode())
conn.send(data.upper())

server.close()