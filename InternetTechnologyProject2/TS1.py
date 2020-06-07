import sys
import socket as mysoc

TS_Dict1 = {}

tsListenport = int(sys.argv[1])

f = open("PROJ2-DNSTS1.txt", 'r')
ts_hostName = f.readlines()
f.close()

for name in ts_hostName:
    TS_Dict1[name.split()[0]] = (name.split()[1], name.split()[2])
   
def TopServer():
    #Try/Except used to handle graceful shutdown of server
    try:

        #open server socket and prepare to accept clients
        try:
            ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))
        server_binding=('',tsListenport)
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
                #send response back to client
                response = server_request + " " + TS_Dict1[server_request][0] + " " + TS_Dict1[server_request][1]
                csockid.send(response.encode('utf-8'))
                print response
            except:
                pass

            

            


    except:

        #close sockets and exit server
        ss.close()
        csockid.close()
        print "\nServer Closing"

    exit()

TopServer()

