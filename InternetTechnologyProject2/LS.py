import sys
import socket as mysoc
from threading import Thread
import time

t1_success = False
t2_success = False
def ts1_thread():
# accepting the clients request and then sending it to the TS1 server
    global t1_success
    try:
        TS1S=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    TS1S_binding=(TS1Host_name,TS1Listenport)
    TS1S.connect(TS1S_binding)

    # here we send it to the TS1 server 
    TS1S.send(server_request.encode('utf-8'))
    

    # here we get it back from the TS1 server 
    TS1S.settimeout(5.0)
    t1_success = False
    try:
        response = TS1S.recv(200).decode('utf-8')
        #send response back to client
        csockid.send(response.encode('utf-8'))
        t1_success = True
    except:
        pass

def ts2_thread():
    # accepting the clients request and then sending it to the TS1 server
    global t2_success
    try:
        TS2S=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    TS2S_binding=(TS2Host_name,TS2Listenport)
    TS2S.connect(TS2S_binding)

    # here we send it to the TS1 server 
    TS2S.send(server_request.encode('utf-8'))
    

    # here we get it back from the TS1 server 
    TS2S.settimeout(5.0)
    t2_success = False
    try:
        response = TS2S.recv(200).decode('utf-8')
        #send response back to client
        csockid.send(response.encode('utf-8'))
        t2_success = True
    except:
        pass



lsListenport = int(sys.argv[1])
TS1Host_name = sys.argv[2]
TS1Listenport = int(sys.argv[3])
TS2Host_name = sys.argv[4]
TS2Listenport = int(sys.argv[5])

# this accepts the clients thread 

#accept client connection and define client socket
try:
    ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
    print('{} \n'.format("socket open error ",err))
server_binding=('',lsListenport)
ss.bind(server_binding)
ss.listen(1)

while True:
    
    csockid,addr=ss.accept()

    #receive and clean request from client
    server_request = csockid.recv(200).decode('utf-8')
    if server_request[-1] == '\r':
        server_request = server_request[:-1]

    # accept the threads back here 
    ts1t = Thread(target=ts1_thread)
    ts1t.setDaemon (True)
    ts2t = Thread(target=ts2_thread)
    ts2t.setDaemon (True)
    ts1t.start()
    ts2t.start()

    ts1t.join()
    ts2t.join()

    if t1_success or t2_success:
        print server_request
        pass
    else:
        csockid.send((server_request + " - Error:HOST NOT FOUND").encode('utf-8'))#FIX ERROR CODE

    csockid.close()





exit()

    













'''
#Set up Root Server "cache" from PROJI-DNSRS
RS_dict = {}

rsListenport = int(sys.argv[1])

f = open("PROJI-DNSRS.txt", 'r')
rs_hostnames = f.readlines()
f.close()

for name in rs_hostnames:
    RS_dict[name.split()[0]] = (name.split()[1], name.split()[2])
    if name.split()[2] == "NS":
        TSHostname = name.split()[0]



def RootServer():
    #Try/Except used to handle graceful shutdown of server
    try:

        #open server socket and prepare to accept clients
        try:
            ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))
        server_binding=('',rsListenport)
        ss.bind(server_binding)
        ss.listen(1)
        host=mysoc.gethostname()
        while True:

            #accept client connection and define client socket
            csockid,addr=ss.accept()


            #receive and clean request from client
            server_request = csockid.recv(200).decode('utf-8')
            if server_request[-1] == '\r':
                server_request = server_request[:-1]

            #form appropriate response based on whether requested hostname is or is not in cache
            try:
               response = server_request + " " + RS_dict[server_request][0] + " " + RS_dict[server_request][1]
            except:
                response = TSHostname + " " + RS_dict[TSHostname][0] + " " + RS_dict[TSHostname][1]


            print response

            #send response back to client
            csockid.send(response.encode('utf-8'))

    except:

        #close sockets and exit server
        ss.close()
        csockid.close()
        print "\nServer Closing"

    exit()

RootServer()

'''