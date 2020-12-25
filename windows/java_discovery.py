#/usr/bin/env python
#This script is used to discovery disk on the server
import subprocess
import os
import socket
import json
import glob

java_names_file='java_names.txt'
javas=[]
if os.path.isfile(java_names_file):
#   print 'java_names_file exists!'
#####
##### here should use % (java_names_file) instead of using the python variable java_names_file directly inside the '''   ''' quotes
#####

   args='''awk -F':' '{print $1':'$2}' %s'''  % (java_names_file)
   t=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]
#elif glob.glob('/opt/xx/*_tomcat') and not os.path.isdir('/opt/logs/logstash') and not os.path.isdir('/opt/app/elasticsearch/config'):
elif glob.glob('/usr/java-jar/*.jar'):
   t=subprocess.Popen('cd /usr/java-jar/ && ls *.jar|grep jar',shell=True,stdout=subprocess.PIPE)

for java in t.stdout.readlines():
    if len(java) != 0:
       javas.append({'{#JAVA_NAME}':java.strip('\n').strip(':')})
print(json.dumps({'data':javas},indent=4,separators=(',',':')))