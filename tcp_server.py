#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:18:28 2018

@author: 3gosc_ai
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(1)
conn,addr=s.accept()
conn.send(b'Please speak')
data=conn.recv(1024).decode('utf8')
print(addr,data)
conn.send(('You send is:'+data).encode('utf8'))
print(type(conn.close()))
