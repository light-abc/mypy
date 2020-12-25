import paramiko
# 获取Transport实例
tran = paramiko.Transport('192.168.0.126',22)
# 连接SSH服务端
tran.connect(username="root", password="Great@1qaz2wsx")
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
# 远程文件路径
remotepath=r"/etc/sysconfig/network-scripts/ifcfg-有线连接_2"
rpath=remotepath[remotepath.rfind('/'):]
file_name=rpath[1:]
# 下载对象保存的文件路径
localpath=r"C:\Users\168\Desktop"'\\'+file_name
# 执行下载动作
sftp.get(remotepath,localpath)
# 关闭Transport实例
tran.close()
print(file_name+"下载成功!")
print("下载路径"+localpath)