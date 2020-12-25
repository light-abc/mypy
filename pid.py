#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal

def kill_process(pid):
    a = os.kill(pid, signal.SIGKILL)
    print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))

def get_pid(port):
	#其中\"为转义"
    pid = os.popen("netstat -nlp | grep :%s | awk '{print $7}' | awk -F\" / \" '{ print $1 }'" % (port)).read().split('/')[0]
    return int(pid)

def run_program(jar_name):
    os.system("nohup java -jar" + jar_name + ">/dev/null" + "2>&1" + "&")
    print("正在启动：%s"%(jar_name))

def main():
    portSet = set()
    portSet.add("3939")
    programSet = set()
    programSet.add("xspch.jar")
    for port in portSet:
        kill_process(get_pid(port))
    for program in programSet:
        run_program(program)

    main()