import threading, sys
import socket as mysoc


rsHostname= sys.argv[1]
rsListenPort = int(sys.argv[2])
tsListenPort = int(sys.argv[3])

def client():
    

# this is where we send the Hostname to the RS server 
    f=open("PROJI-HNS.txt","r")
    Host_names = f.readlines()
    f.close()

    f=open("RESOLVED.txt", "w")

    
    for request in Host_names:
        try:
            rs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))
        server_binding=(rsHostname,rsListenPort)
        rs.connect(server_binding)
        if request[-1] == "\n":
            request = request[:-1]
        
        request = request.lower()

        rs.send(request.encode('utf-8'))
        response = rs.recv(200).decode('utf-8')

        

        #  look at the response and look for the last element to check if it was 
        #  an A or an NS 


        if response.split()[-1]=="NS":
            try:
                ts=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            except mysoc.error as err:
                print('{} \n'.format("socket open error ",err))
            tsserver_binding=(response.split()[0],tsListenPort)
            ts.connect(tsserver_binding)
            ts.send(request.encode('utf-8'))
            response = ts.recv(200).decode('utf-8')
        

        f.write(response+ "\n")
        
            
    


        
        rs.close()
    f.close()
    exit()



client() 
