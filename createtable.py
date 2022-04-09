import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='test')
cur=db.cursor()
cur.execute("drop table if exists Item")
cur.execute('create table Item (Itemno int(4) PRIMARY KEY,Itemname varchar(20),Price decimal(9,2),Quantity int(6))')
print("Table created")
db.close()
