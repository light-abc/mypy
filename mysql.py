import pymysql

conn = pymysql.connect(
    host='192.168.0.146',
    port=3306,
    user='root',
    password='sunnyRM@123',
    charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

s = """SHOW DATABASES"""
# 使用 execute()  方法执行 SQL 查询

a = cursor.fetchone(s)
#cursor.execute(create_dep)
print(a)
#results = cursor.fetchall()
# 使用 fetchone() 方法获取单条数据.
# sql = """CREATE TABLE EMPLOYEE (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,
#         SEX CHAR(1),
#         INCOME FLOAT )"""

cursor.close()
conn.close()