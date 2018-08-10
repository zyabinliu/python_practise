#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:28:39 2018

@author: 3gosc_ai
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))
print(s.recv(1024).decode('utf8'))

data=input('Please input:')
print(data,type(data))
s.send(data.encode('utf8'))
print(s.recv(1024).decode('utf8'))
s.close()
