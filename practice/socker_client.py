#author:xm
#coding:utf-8

import socket

client = socket.socket() #socket参数默认情况下是ipv4，tcp协议
client.connect(("localhost",6369))

client.send("你好世界".encode("utf-8"))
data = client.recv(1024)

print(data.decode())

client.close()