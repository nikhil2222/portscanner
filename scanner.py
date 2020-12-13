#!/bin/python
import sys
import socket
from datetime import datetime

#define our target

if len(sys.argv)==2:
           target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:
           print("Invalid amount of arguments")
           
print("-" *50)
print("scanning target"+target)
print("Time started:" + str(datetime.now())) 
print("-" *50) 

try:
            for port in range(50,85):
                        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)
                        result = s.connect_ex((target,port)) #return an error indicaor
                        if result == 0:
                                 print("Port {} is open".format(port))
                        s.close()
except KeyboardInterrupt:
        print("\n exit")
        sys.exit()

except socket.gaierror:
        print("host name cannot be resolved")
        sys.exit()

except socket.error:
        print("coudnt connect to server")
        sys.exit()                                        
                                                    
           
           
