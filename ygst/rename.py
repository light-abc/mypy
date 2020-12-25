import os
import time
import datetime
#
# def getYesterday(today):
#     yesterday = datetime.datetime(int(today[:4]), int(today[4:6]), int(today[6:])) + datetime.timedelta(days=-1)
#     yesterday = str(yesterday)
#
#     return '%s%s%s' % (yesterday[:4],yesterday[5:7],yesterday[8:10])
#
# print(getYesterday())

#获取当前时间
today = datetime.datetime.now()
print(today)
#计算偏移量
offset = datetime.timedelta(days=-5)
#获取想要的日期的时间
re_date = (today + offset).strftime('%m%d')

print(re_date)
# dir = "/usr/"
# current_file_name='back-center.jar'
# file_name=current_file_name[:-4]+time.strftime('%m%d.jar')
# new_file_name=current_file_name[:-4]+time.strftime('%m%d.jar')
#
# os.rename(current_file_name,new_file_name)
# file_list=(os.listdir(dir))
# print(file_list)
# for item in file_list:
#     if item.endswith('.jar'):
#         shutil.move('/usr/%s' % item, '/usr/%s' % item[:-5]+time.strftime('%m%d.jar'))
#         print(item.endswith('.jar'))
