import sys
import socket as mysoc



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
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',rsListenport)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    while True:
        csockid,addr=ss.accept()

        server_request = csockid.recv(200).decode('utf-8')
        if server_request[-1] == '\r':
            server_request = server_request[:-1]

        try:
           response = server_request + " " + RS_dict[server_request][0] + " " + RS_dict[server_request][1]
        except:
            response = TSHostname + " " + RS_dict[TSHostname][0] + " " + RS_dict[TSHostname][1]

        print response

        csockid.send(response.encode('utf-8'))



        csockid.close()

    exit()

RootServer()