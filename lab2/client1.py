import socket
import threading
import random
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
CLIENT_IP = "127.0.0.1"

def ReceiveData(sock):
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass

def RunClient():
    port = random.randint(6000,10000)
    print(f'Client IP-> {CLIENT_IP} Port-> {port}')
    server = (SERVER_IP, SERVER_PORT)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((CLIENT_IP, port))

    name = input('Please write your name here: ')
    if name == '':
        name = 'Guest'+str(random.randint(1000,9999))
        print('Your name is:'+name)
    s.sendto(name.encode('utf-8'),server)
    threading.Thread(target=ReceiveData,args=(s,)).start()
    while True:
        data = input()
        if data == 'qqq':
            break
        elif data=='':
            continue
        data = '['+name+']' + '->'+ data
        s.sendto(data.encode('utf-8'),server)
    s.sendto(data.encode('utf-8'),server)
    s.close()
    os._exit(1)


if __name__ == '__main__':
    RunClient()