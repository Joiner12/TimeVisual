#-*- coding:utf-8 -*-
"""
    网络通信服务器
"""
import socket
import threading
import time

log_file = r"D:\Code\TimeVisual\ToolPy\chongbuluo.log"


#每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    time.sleep(1)
    print("服务器:发送数据包")
    # 打开文件并发送数据
    with open(log_file, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                print("数据包发送完成")
                break
            sock.sendall(data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 获取以太网IPV4地址
import socket


# 获取以太网IPv4地址
def get_ethernet_ipv4():
    try:
        # 创建套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到百度服务器
        s.connect(('www.baidu.com', 80))
        # 获取套接字的本地协议地址，即以太网IPv4地址
        ethernet_ipv4 = s.getsockname()[0]
        s.close()
        return ethernet_ipv4
    except:
        return None


# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听的地址和端口
ethernet_ipv4 = get_ethernet_ipv4()
if ethernet_ipv4 is not None:
    print('ipv4:', ethernet_ipv4)
    s.bind((ethernet_ipv4, 9999))
else:
    s.bind(('127.0.0.1', 9999))

# 开始监听端口
s.listen(5)
print('Waiting for connection...')

# 等待连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
