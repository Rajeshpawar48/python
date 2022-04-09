import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='test')
cur=db.cursor()
cur.execute("select * from Item")
print('Item no\t\t     Item name\t\t     Price\t\t     Quantity')
for row in cur.fetchall():
    print(row[0],'\t\t    ',row[1],'\t\t    ',row[2],'\t\t    ',row[3])
db.close()
