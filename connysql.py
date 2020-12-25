import pymysql

# 建立连接
conn = pymysql.connect(
    host='192.168.0.105',
    port=8066,
    user='root',
    passwd='Great@1qaz2wsx',
    database='ygst-center'
)

# 创建操作数据库的游标
cursor = conn.cursor()

# 编写创建表的SQL语句
use = """use zabbix"""
show = """show databases"""
show_db = """show tables"""
con = """show variables like '%con%'"""

# 通过cursor执行SQL语句
#cursor.execute(use)
cursor.execute(show_db)
#cursor.execute(show_db)

print(cursor.fetchall())
# 确认
conn.commit()

# 关闭
cursor.close()
conn.close()