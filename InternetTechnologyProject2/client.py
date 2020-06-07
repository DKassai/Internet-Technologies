import threading, sys
import socket as mysoc


rsHostname= sys.argv[1]
LsListenPort = int(sys.argv[2])


def client():
    

    #read in hostnames to be queries

    f=open("PROJ2-HNS.txt","r")
    Host_names = f.readlines()
    f.close()

    #open file for output to be written to
    f=open("RESOLVED.txt", "w")

    
    #iterate through list of hostnames
    for request in Host_names:
        if request[-1] == "\n":
            request = request[:-1]        
        request = request.lower()

        #open client socket
        try:
            LS=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))
        server_binding=(rsHostname,LsListenPort)

        #connect to Root Server
        LS.connect(server_binding)

        #send request to Root Server and wait for response
        LS.send(request.encode('utf-8'))
        response = LS.recv(200).decode('utf-8')

        #close Root Server socket
        LS.close()

    
        
        #record query response into RESOLVED.txt
        f.write(response+ "\n")
        
    #close output file and exit client program
    f.close()
    print("Responses Successfully Written To:\tRESOLVED.txt\nClient Closing")
    exit()



client() 
