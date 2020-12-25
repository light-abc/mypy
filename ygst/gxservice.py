import os
import sys
import shutil
import glob
import time
import re

date=time.strftime('%m%d')
dir = r"/usr/java-jar/"
fname = input("请输入更新服务名: ")
mname = time.strftime('work-center'+'%m%d'+'.jar')
path = dir+fname

os.chdir(dir)
file_list = os.listdir()
listdir=['auth-server.jar', 'file-center.jar', 'log-center.jar', 'queue-center.jar', 'statistics-center.jar', 'supervise-center.jar', 'system-center.jar', 'user-center.jar', 'work-center.jar']


def plmv():
    flist = glob.glob('*.jar')
    for file in flist:
        shutil.move(file, date)
        print(sys.argv)