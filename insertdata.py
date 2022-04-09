import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='test')
cur=db.cursor()
try:
    cur.execute("insert into Item values(101,'Geometry Box ','50',100)")
    cur.execute("insert into Item values(102,'Soap','100',50)")
    cur.execute("insert into Item values(103,'Perfume','150',25)")
    cur.execute("insert into Item values(104,'Pen','50',200)")
    cur.execute("insert into Item values(105,'Pencil','20',100)")
    db.commit()
except:
    db.rollback()
print("Data inserted")
db.close()
