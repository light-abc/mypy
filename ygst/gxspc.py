import os
import shutil
import time
import re

dir = r"/usr/java-jar/"
fname = 'work-center'+'.jar'
mname = time.strftime('work-center'+'%m%d'+'.jar')
path = dir+fname

os.chdir(dir)
file_list = os.listdir()
listdir=['file-center.jar', 'log-center.jar', 'queue-center.jar', 'statistics-center.jar', 'supervise-center.jar', 'system-center.jar', 'user-center.jar', 'work-center.jar', 'auth-server.jar']

def rename():
    if os.path.isfile(path):
        shutil.move(fname, mname)
        print(mname.endswith('.jar'))
        if os.path.isfile(mname):
            print(fname+'重命名成功!')

def plgm():
    if file_list == listdir:
        for item in file_list:
            mitem = item[:-4]
            mname = mitem + time.strftime('%m%d') + '.jar'
            if item.endswith('.jar'):
                shutil.move(item, mname)
                print(mname, item.endswith('.jar'))
        print(os.listdir())
    else:
        print(os.listdir())
        exit()
        # for item in file_list:
        #     mitem = re.sub(r'\d', "", item)
        #     #mname = mitem + '.jar'
        #     if item.endswith('.jar'):
        #         shutil.move(item, mitem)
        #         print(item.endswith('.jar'))

def gxjar():
    os.system('killall java')
    os.system('for i in {auth-server,user-center,log-center,file-center,work-center,\
    supervise-center,system-center,statistics-center,queue-center};\
    do `nohup java -jar /usr/java-jar/$i.jar >/dev/null 2>&1 &` sleep 3;done')

def jps():
    os.system('jps;ps -ef|grep java')

if __name__ == '__main__':
    plgm()
