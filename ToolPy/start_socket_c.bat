@echo off
cd D:\Code\TimeVisual\ToolPy\
echo �����ͻ���
python socket_client.py
ping 127.0.0.1 -n 2 > nul
pause