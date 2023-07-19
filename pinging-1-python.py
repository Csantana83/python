import os

hostname = "192.168.1.78" #example
response = os.system("ping -c 1 " + hostname) # -c linux // -n Windows

#and then check the response...
if response == 0:
    print(hostname, 'is up!')
    ip_name = os.system("hostname -f")
    print(ip_name)
else:
    print(hostname, 'is down!')