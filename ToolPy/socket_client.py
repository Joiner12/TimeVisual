#-*- coding:utf-8 -*-
"""
    网络通信客户端
"""
import socket
import time

recv_log = r"D:\Code\TimeVisual\ToolPy\recv.log"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False
connecting_cnt = 0
while not connected and connecting_cnt < 5:
    try:
        # 建立连接:
        s.connect(('192.168.1.105', 9999))
        connected = True
    except socket.error:
        print("连接失败,1秒后重试...")
        time.sleep(1)
    connecting_cnt += 1
# 接受数据文件
print("开始接收数据包...")
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
# 把接收的数据写入文件:

with open(recv_log, 'wb') as f:
    for d in buffer:
        f.write(d)
print("数据接收完成!")
s.close()
