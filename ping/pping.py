#!/usr/bin/env python3
import subprocess
import platform

current_ip_address = open("hosts.txt","r")
 
def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:  
        return False
for each in current_ip_address:
    if ping_ip(each):
        response=open("response.txt","w")                 
        print (f"{each} is available")
        response.write(f"{each} is available\n")
        response.close()
    else:
        fail=open("fail.txt","w")                 
        print (f"{each} is not available")
        fail.write(f"{each} is not available\n")
        fail.close()
