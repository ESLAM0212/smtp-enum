#!/usr/bin/python
import socket
import sys , time

if len(sys.argv) != 3:
   print "USES: ./smtp-enum.py <IP> <USERS_FILE> "
   exit(0)

ip=sys.argv[1]
users=sys.argv[2]
print "wait..."

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connect=s.connect((ip,25))
banner=s.recv(1024)
print banner

user=open(users).readlines()
for u in user:
   u=u.strip()
   s.send("VRFY "+u+"\r\n")
   result=s.recv(1024)
   print result
   time.sleep(3)
s.close()
