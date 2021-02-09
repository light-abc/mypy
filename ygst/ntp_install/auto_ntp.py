import paramiko

import time

import sys

import socket

host  =  open(sys.argv[1])

host_list = []

username="root"

for  hosta in  host.readlines():

    host_list.append(hosta.strip().split())

f = open('log.txt', 'a')

cmd = open(sys.argv[2])

for hostname,password in host_list:

    ssh_client = paramiko.SSHClient()

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

       ssh_client.connect(hostname=hostname, username=username, password=password)

       print("Successfull connected to ", hostname)

       cmd.seek(0)

       stdin, stdout, stderr = ssh_client.exec_command('hostname')

       f.write(hostname + ' ' + stdout.read().decode('utf-8') + "\n")

       for ccc in cmd.readlines():

           c = ccc.strip()

           stdin, stdout, stderr = ssh_client.exec_command(c)

           f.write(stdout.read().decode('utf-8') + "\n")

           f.write(stderr.read().decode('utf-8') + "\n")

    except paramiko.ssh_exception.AuthenticationException:

           print("User authentication failed for " + username)

    except socket.error:

           print(hostname + " is not reachable.")

cmd.close()

f.close()

ssh_client.close()