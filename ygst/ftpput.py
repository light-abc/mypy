import paramiko
import os
#获取Transport实例
tran = paramiko.Transport('192.168.0.126',22)
#连接SSH服务端
tran.connect(username = "root", password = "Great@1qaz2wsx")
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
#设置上传的本地/远程文件路径
localpath=r"D:\1275757008\FileRecv\0612\back-center.jar"   ##本地文件路径
remotepath=r"/usr/back-center.jar"   ##上传对象保存的文件路径
#执行上传动作
sftp.put(localpath,remotepath)

tran.close()