import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.128', username='root', password='a', port=22)

stdin, stdout, stderr = ssh.exec_command('ip a')
out = stdout.read()
err = stderr.read()
print(out)
print(err)
out.decode()
ssh.close()

# result = ssh.exec_command('id root')
#
# print(len(result))
#
# result[1].read()
# result[2].read()
