#!/usr/bin/env python
# coding:utf-8
import xlwt
# import xlsxwriter
import time
import os
# import openpyxl

os.chdir(r'C:\Users\168\Documents')
date=time.strftime('%m%d')
# style = "font:colour_index red; align: wrap on, vert center, horiz center;"
# style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
# font = xlwt.Font() # 为样式创建字体
# pattern = xlwt.Pattern()
# pattern.pattern_fore_colour=
# alignment = xlwt.Alignment()
# alignment.horz = 0x02      # 设置水平居中
# alignment.vert = 0x01      # 设置垂直居中
# alignment = alignment
# red_style = xlwt.easyxf(style)
title_style = xlwt.easyxf('font: height 220, name 宋体;align: vert center, horiz center;pattern: pattern solid, fore_colour 22;borders: left 1, right 1, top 1, bottom 1;')
t1_style = xlwt.easyxf('font: height 220, name 宋体, colour_index black;align: wrap on, vert center, horiz center;borders: left 1, right 1, top 1, bottom 1;')
txt_style = xlwt.easyxf("font: height 220, name 宋体, colour_index black;align: wrap on, vert center, horiz center;borders: left 1, right 1, top 1, bottom 1;")
# num_format_str='0.00%'
ip=["10.0.18.160","10.0.18.161","10.0.18.162","10.0.18.163","10.0.18.164","10.0.18.165","10.0.18.166","10.0.18.167","10.0.18.168","10.0.18.169","10.0.18.170","10.0.18.171","10.0.18.172","10.0.18.173","10.0.18.174","10.0.18.175","10.0.18.176","10.0.18.177","10.0.18.178","10.0.18.179","10.0.18.180","10.0.18.181","10.0.18.182","10.0.18.183","10.0.18.184","10.0.18.185","10.0.18.186","10.0.18.187","10.0.18.188","10.0.18.189","10.0.18.190","10.0.18.191","10.0.18.192","10.0.18.193","10.0.18.194","10.0.18.195","10.0.18.196","10.0.18.197","10.0.18.198","10.0.18.199","10.0.18.200","10.0.18.201","10.0.18.202","10.0.18.203","10.0.18.204","10.0.18.205","10.0.18.206","10.0.18.207","10.0.18.208","10.0.18.209","10.0.18.210","10.0.18.211","10.0.18.212","10.0.18.213","10.0.18.214","10.0.18.215","10.0.18.216","10.0.18.217","10.0.18.218","10.0.18.219","10.0.18.220","10.0.18.221","10.0.18.222","10.0.18.223","10.0.18.227","10.0.18.228","10.0.18.229","10.0.18.230","10.0.18.231","10.0.18.232","10.0.18.233","10.0.18.234","10.0.18.235","10.0.18.236","10.0.18.237","10.0.18.238","10.0.18.239","10.0.18.240","10.0.18.241","10.0.18.242","10.0.18.243","10.0.18.244","10.0.18.245","10.0.18.246","10.0.18.247"]
fwqm=["Nginx反向代理","Nginx反向代理","前端服务器","前端服务器","前端服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","动态网关服务器","微服务服务器","微服务服务器","微服务服务器","微服务服务器","微服务服务器","微服务服务器","跑缓存线程","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","前端服务器","前端服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","文件服务器","缓存服务器","缓存服务器","缓存服务器","缓存服务器","日志Mycat服务器","日志Mycat服务器","应用Mycat服务器","应用Mycat服务器","消息队列服务器","注册中心","定时任务中心","注册中心","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","应用数据库","微服务服务器","微服务服务器","监控服务器","日志数据库","日志数据库"]
hostn=["Nginx1","Nginx2","Back-C1","Back-C2","Back-C3","GW1","GW2","GW3","GW4","GW5","GW6","GW7","GW8","GW9","GW10","GW11","GW12","MS1","MS2","MS3","MS4","MS5","MS6","finance-task","DB1","DB2","DB3","DB4","DB5","DB6","DS1","DS2","DS3","DS4","DS5","DS6","Back-C4","Back-C5","File1","File2","File3","File4","File5","File6","File7","File8","File9","File10","File11","File12","File13","File14","RD1","RD2","RD3","RD4","Log-Mycat1","Log-Mycat2","DB-Mycat1","DB-Mycat2","activemq","eureka","task","eureka2","DSS1","DSS2","DSS3","DSS4","DSS5","DSS6","DSSS1","DSSS2","DSSS3","DSSS4","DSSS5","DSSS6","DB7","DS7","DSS7","DSSS7","MS7","MS8","zabbix","LDB1","LDB2"]
val1='无异常'
val2='无'
mz='黄亮亮'

def wxls():
    title = ['ip地址','服务器名称','主机名','cpu平均利用率','内存平均利用率','磁盘使用情况','网络连接','日志检查','系统漏洞','软件运行情况','异常问题记录','巡检记录人']
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('巡检记录')
    for i, val in enumerate(title):
        first_col = worksheet.col(i)
        first_col.width = 220 * 24
        worksheet.write(0, i, label=val,style=title_style)
    for i in range(0, len(ip)):
        worksheet.write(i+1, 0, ip[i], t1_style)
    for i in range(0, len(fwqm)):
        worksheet.write(i+1, 1, fwqm[i], t1_style)
    for i in range(0, len(hostn)):
        worksheet.write(i+1, 2, hostn[i], t1_style)

    with open('xunjian.txt', 'r+',encoding='utf-8') as f:
        s1 = f.readlines()
    f.close()

    for i,s in enumerate(s1):
        # cpu=s[:5]
        # cpu1=s[:2]
        # mem=s[5:9]
        # mem1=s[3:7]
        # disk=s[-3:-1]
        cpu=s[:6]
        mem=s[6:13]
        disk=s[-7:-1]

        if i in range(38, 52):
            worksheet.write(i+1, 3, cpu.rstrip().lstrip(), txt_style)
            worksheet.write(i+1, 4, mem.rstrip().lstrip(), txt_style)
            worksheet.write(i+1, 5, disk.rstrip().lstrip(), txt_style)
        else:
            worksheet.write(i+1, 3, cpu.rstrip().lstrip(), txt_style)
            worksheet.write(i+1, 4, mem.rstrip().lstrip(), txt_style)
            worksheet.write(i+1, 5, disk.rstrip().lstrip(), txt_style)
        worksheet.write(i+1, 6, val1, t1_style)
        worksheet.write(i+1, 7, val1, t1_style)
        worksheet.write(i+1, 8, val1, t1_style)
        worksheet.write(i+1, 9, val1, t1_style)
        worksheet.write(i+1, 10, val2, t1_style)
        worksheet.write(i+1, 11, mz, t1_style)
    txt_style.num_format_str = ('0.00%')
    t = time.strftime('%H')
    if t <= '12':
        t='9'
    elif t > '12':
        t='17'
    name = '巡检记录--'+t+'点 - '+ date +'.xlsx'
    workbook.save(name)

wxls()