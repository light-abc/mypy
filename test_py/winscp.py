import subprocess

# subprocess.check_output('WinSCP.com /command "open sftp://userName:passWord@IPAddress -hostkey=""ssh-rsa 2048 xx:xx:xx:7x:x0:18:94:01:xx:xc:e1:ae:xx:x:xx:x5""" "get file_path" "exit"', cwd="C:\\Program Files (x86)\\WinSCP", shell=True)

subprocess.check_output('WinSCP.com /ls "open sftp://root:redmi1903@192.168.0.126 -hostkey=""ssh-rsa 2048 35:e7:b4:de:51:f6:02:93:3c:7a:1c:11:a7:67:20:fb""" "/root" "exit"', cwd="C:\\Program Files (x86)\\WinSCP", shell=True)
