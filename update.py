##Aim: Fill up totalprice = price * quantity.
##INPUT:
import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='test')
cur=db.cursor()
cur.execute("update Item set Price=Price-25 where Itemno=101")
##cur.execute("update Item set Totalprice=Price*Quantity where Itemno=102")
##cur.execute("update Item set Totalprice=Price*Quantity where Itemno=103")
##cur.execute("update Item set Totalprice=Price*Quantity where Itemno=104")
##cur.execute("update Item set Totalprice=Price*Quantity where Itemno=105")
print('Totalprice column filled')
db.close()
