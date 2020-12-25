import xlwt
import time
import os
# import xlsxwriter
# from io import StringIO

os.chdir('C:\\Users\\168\\Documents')
datetime=time.strftime('%m%d %H%M')
timeh=time.strftime('%H')
#style = "font:colour_index red; align: wrap on, vert centre, horiz center;"
style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = '宋体'
font.charset = '11'
#font.bold = True # 加粗
#font.underline = True # 下划线
#font.italic = True # 斜体字
style.font = font # 设定样式

def getlist():
    with open('monitor.txt', 'r+', encoding='utf-8') as f:
        s1 = f.readlines()
    f.close()
    s2 = []
    for i in s1:
        s2.append(i[5:16])
        print(s2)
    return s2

def fenge():  # 分割
    list0 = []  # 存贮空格行
    for num, val0 in enumerate(getlist()):
        #if val0.split('')[2] in '主机名':
            list0.append(num)
    list0.append(len(getlist()))
    list1 = []  # 存贮内容
    for num1, val1 in enumerate(list0[1:]):
        temp = getlist()[list0[num1]:list0[num1 + 1]]
        list1.append(temp)
    return list1

def wxls():  # 写入表格
    title = ['IP地址', '主机名', 'cpu平均利用率', '内存平均使用率', '磁盘使用率']
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    #worksheet.write(1, 0, 'Formatted value', style)
    for i1, val in enumerate(title):
        worksheet.write(0, i1, label=val, style=style)
        first_col = worksheet.col(i1)
        first_col.width = 180 * 20

    name = '巡检记录--17点' + datetime +'.xls'
    workbook.save(name)
wxls()