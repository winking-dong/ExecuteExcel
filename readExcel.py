# -*- coding: utf-8 -*-
import xlsxwriter as xw
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
        #表示已经取完结果集https://blog.csdn.net/qq20004604/article/details/78473273/
        break
    print(res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')




def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '酒店', '价格']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):

        insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
        print(insertData)
        row = 'A' + str(i)
        print(row)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]
fileName = '测试.xlsx'

xw_toExcel(testData, fileName)