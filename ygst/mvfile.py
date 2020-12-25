import os
import shutil
import time
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.126', username='root', password='Great@1qaz2wsx', port=22)

dir = r"/usr/"
#file= 'back-center.jar'
#filen= file[:-5]+time.strftime('%m%d.jar')
#result = ssh.exec_command('')

#print(len(result))
# result[1].read()
# result[2].read()

file_list=(os.listdir(dir))
for item in file_list:
    if item.endswith('.jar'):
        shutil.move('/usr/%s' % item, '/usr/%s' % item[:-5]+time.strftime('%m%d.jar'))
        print(item.endswith('.jar'))

stdin, stdout, stderr = ssh.exec_command()
out = stdout.read()
err = stderr.read()
print(out)
print(err)
out.decode()
ssh.close()