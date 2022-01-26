import pymysql
#打开数据库连接
conn = pymysql.connect(host='localhost',
                       user="root",
                       passwd="root",
                       db="student")

cur=conn.cursor()

cur.execute("select * from student;")
while 1:
    res=cur.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print(res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')

