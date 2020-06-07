import sys
import socket as mysoc

TS_Dict = {}

tsListenport = int(sys.argv[1])

f = open("PROJI-DNSTS.txt", 'r')
ts_hostName = f.readlines()
f.close()

for name in ts_hostName:
    TS_Dict[name.split()[0]] = (name.split()[1], name.split()[2])
   
def RootServer():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',tsListenport)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    while True:
        csockid,addr=ss.accept()

        server_request = csockid.recv(200).decode('utf-8')
        if server_request[-1] == '\r':
            server_request = server_request[:-1]

        try:
           response = server_request + " " + TS_Dict[server_request][0] + " " + TS_Dict[server_request][1]
        except:
            response = server_request +  " - Error:HOST NOT FOUND"

        print response

        csockid.send(response.encode('utf-8'))



        csockid.close()

    exit()

RootServer()
'''
import socket as mysoc

def TopServer():
 
 
 
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50008)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    localhost_ip=(mysoc.gethostbyname(host))
    csockid,addr=ss.accept()
    while True:

        exit()

TopServer()
'''