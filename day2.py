import pymysql
conn=pymysql.connect(host="localhost",user="Theja1684",
                     password="Teju26092006")
print("connected")
cur=conn.cursor()
cur.execute("use day1")
cur.execute("select * from schooling")
tables=cur.fetchall()
for x in tables:
    print(x)