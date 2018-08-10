import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.43.237',4000))
while True:
    data=input('client:').encode('utf8')
    s.send(data)
    data=s.recv(1024)
    print(data.decode('utf8'))
    if (data.decode('utf8'))=='bye':
        s.close()
        break
