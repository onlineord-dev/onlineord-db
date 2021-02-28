import pyodbc
import pandas as pd
import numpy as np

driver='{MySQL ODBC 8.0 ANSI Driver}'
server='den1.mysql4.gear.host'
database='onlineord'
username='onlineord'
password='Bd4tO--2FL7V'

cnxn = pyodbc.connect(Driver='{MySQL ODBC 8.0 ANSI Driver}',Server=server,Database=database,Uid=username,Pwd=password)
cursor = cnxn.cursor()


excel = pd.read_excel(r'C:\Users\andri\Desktop\PW\Data\food.xlsx')

def LoadData(data):
    for index, row in data.iterrows():
       
        sql = "INSERT food(Price,Name,weight) VALUES ('{}', '{}', '{}')".format(row["Price"],row["Name"],row["Weight"])
        cursor.execute(sql)

LoadData(excel)

cursor.execute("SELECT * FROM food")
for row in cursor:
    print(row)

cnxn.commit()
cnxn.close()