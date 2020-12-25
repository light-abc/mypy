import os,time,pymysql

user='user'
pwd='pwd'

def getDatabaseNames():
    conn = pymysql.connect("localhost", user, pwd, use_unicode=True, charset="utf8")
    cur = conn.cursor()
    cur.execute('show databases;')
    dbs = cur.fetchall()
    cur.close()
    conn.close()
    return dbs

#path trim一下然后创建
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':
    timestr = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    folder = "mysql_data_bak/"+timestr
    mkdir(folder)

    dbs = getDatabaseNames()
    print(dbs)
    for db in dbs:
        try:
            dbname = db[0]
            #排除自带的db
            if dbname=="mysql" or dbname=="performance_schema" or dbname=="information_schema" or dbname=="sys":
                continue
            #导出db
            cmd = "mysqldump -u%s -p%s %s > %s/%s.sql" % (user, pwd, dbname, folder, dbname)
            print(cmd)
            os.system(cmd)
        except Exception as e:
            print(e)