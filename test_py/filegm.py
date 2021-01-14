#endswith 截取文件后缀
import os
path="data"
for curDir, dirs, files in os.walk(path):
    [print(os.path.join(curDir, file)) for file in files  if file.endswith(".xlsx")]

# 使用os.walk输出某个目录下的所有文件
path="data"
for curDir, dirs, files in os.walk(path):
    for _dir in dirs:
        print(os.path.join(curDir, _dir))

import pandas as pd
import numpy as np
import os,openpyxl
#移动符合条件文件，并删除二级文件夹和多余文件
def move_file(file_path,_new_path,date_xl_str):

    #本月文件移动至对应新建文件夹，非本月文件直接删除
    for curDir, dirs, files in os.walk(file_path):
        for file in files:
            old_path = os.path.join(curDir, file)
            new_path = os.path.join(_new_path, file)
            file_date=file.split("_")[-1][:10]
            try:
                os.rename(old_path,new_path) if file_date in date_xl_str else os.remove(old_path)
            except:
                os.remove(old_path)

    #移除子文件夹
    for curDir, dirs, files in os.walk(file_path):
        for _dir in dirs:
            os.removedirs(os.path.join(curDir, _dir))
    os.mkdir("data")

#文件去重-相同日期文件
def qch_date(file_path):
    wj_names=os.listdir(file_path)
    wj_list=[]
    num=0
    for wj in wj_names:
        new_wj=wj[:-11]
        if new_wj not  in wj_list:
            wj_list.append(new_wj)
        else:
            os.remove(file_path+"\\"+wj)
            num+=1
    return num

#更新数据源
def refresh_data(file_path,sheet_name,data):
    book=openpyxl.load_workbook(file_path)
    writer=pd.ExcelWriter(file_path,engine="openpyxl")

    #在ExcelWriter的源代码中，它初始化空工作簿并删除所有工作表，
    #writer.book = book将原来表里面的内容保存到writer中
    writer.book=book

    #activate激活指定sheet工作表
    ws=book[sheet_name]

    #清空当前活动表数据
    for row in ws.iter_rows():
        for cell in row:
            cell.value=None

    #dataframe行列数
    idx_num,col_num=data.shape

    #新数据写入当前活动表-注意索引偏移
    for i in  range(1,idx_num+1):
        for j in range(1,col_num+1):
            ws.cell(row=i,column=j).value=data.iloc[i-1,j-1]

    #保存关闭writer
    writer.save()
    writer.close()

    return None

#文件检查
def check_file(file_path,check_file="文件检查.xlsx"):
    wj_names=os.listdir(file_path)
    data=pd.DataFrame([wj.split("_")[2:] for wj in wj_names],columns=["店铺名称","日期"])
    data['日期']=data['日期'].str[:10]

    #标题columns放到dataframe中
    nind=data.index.insert(0,'0')
    data1=data.reindex(index=nind)
    data1.loc['0']=data.columns
    data1.reset_index(drop=True,inplace=True)

    #刷新数据源
    refresh_data(check_file,"数据源",data1)

    return None

file_path="data"
#日期格式：xxxx-xx eg:2020-07-01
start_date=input("请输入开始日期：")
end_date=input("请输入开始日期：")

#生成日期区间-字符串类型
date_xl_str=[str(i)[:10] for i in pd.date_range(start_date,end_date,freq='D')]

#创建指定文件夹
new_path=start_date+"~"+end_date
try:
    os.mkdir(new_path)
except:
    print("文件夹 【%s】 已存在"%new_path)

#移动符合条件文件，并删除二级文件夹和多余文件
move_file(file_path,new_path,date_xl_str)

#文件去重
num=qch_date(new_path)
print("去除重复文件 %s 个"%num)

#文件检查
check_file(new_path)