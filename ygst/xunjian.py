import os
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in range(198,211):
    ssh.connect(hostname='10.0.18.'+str(i), username='administrator', password='zaq1)OKM', port=22)
    stdin, stdout, stderr = ssh.exec_command("powershell.exe C:'\Program Files\Zabbix Agent\bin\zabbix_get' -s 127.0.0.1 -k 'system.cpu.util'")

    out = stdout.read()
    err = stderr.read()

    print(out)
    print(err)
    out.decode()
ssh.close()