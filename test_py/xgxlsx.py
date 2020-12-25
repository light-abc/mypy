import openpyxl

workbook = openpyxl.load_workbook("DataSource\myfile.xlsx")
worksheet = workbook.worksheets[0]

# 在第一列之前插入一列
worksheet.insert_cols(1)  #

for index, row in enumerate(worksheet.rows):
    if index == 0:
        row[0].value = "编号"  # 每一行的一个row[0]就是第一列
    else:
        row[0].value = index
# 枚举出来是tuple类型，从0开始计数

workbook.save(filename="DataSource\myfile.xlsx")