#!/usr/bin/env python
import os
import subprocess

access_log=os.system("ls -rt /usr/local/nginx/logs/access*.log")
an=os.system("ls /usr/local/nginx/logs/access*.log|wc -l")
os.chdir('/usr/local/nginx/logs')
a=0
b=0

for i, in access_log:
	PV=os.system("sed -n '$=' i")
	UV=os.system("awk '{IP[$2]++} END{print length(IP)}' $i`")
	print(i+'PV次数'+PV)
	print(i+'UV次数'+UV)
	a=(a+PV)
	b=(b+UV)
	#PV=`eval echo '$'"PV$i"`
print("一周总共PV$a")
print("一周总共UV$b")
print("本周平均页面浏览次数PV"+a/an)
print("本周平均独立访客UV"+b/an)
print("本周人均访问次数"+a/b)