import pymysql
import csv
import pandas

# 打开数据库连接
conn = pymysql.connect(
    host="autodealerpricerw.db2.sohuno.com",
    port=3306,
    user="dealer_price_rw",
    password="W0Jj9m9Vby77RJ0",
    database="dealer_price"
)

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# Sql
sql = "SELECT feel_type,feel_content FROM spider_koubei_user_comment_item"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

except:
    print("Error: unable to fetch data")

# 文件路径
path = "D://PYTHON//word2vec//data//all_data.csv"

type_list = ["外观","内饰","空间","动力","操控","油耗","舒适性","性价比","售前售后"]

with open(path,"w",newline='') as file:
    wcsv = csv.writer(file)
    for row in results:
        if row and row[0] in type_list:
            print(row)
            wcsv.writerow(row)

