#server
import socket
from threading import Thread
def forward(conn):
    while True:
            data=conn.recv(1024)
            print(data.decode('utf8'))
            data=input('server:').encode('utf8')
            conn.send(data)
            if (data.decode('utf8'))=='bye':
                conn.close()
                break
            
if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',4000))
    s.listen(5)
    while True:
        ss,addr=s.accept()
        t=Thread(target=forward,args=(ss,))
        t.start()
