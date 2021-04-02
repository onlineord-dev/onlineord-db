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


excel = pd.read_excel(r'C:\Users\andri\Desktop\PW\Data\organization.xlsx')

def LoadData(data):
    for index, row in data.iterrows():
       
        sql = "INSERT organization(Name,Address,Email,Passwords,Phone_number) VALUES ('{}', '{}', '{}', '{}','{}')".format(row["Name"],row["Address"],row["Email"],row["Passwords"],row["Phone_number"])
        cursor.execute(sql)

LoadData(excel)

cursor.execute("SELECT * FROM organization")
for row in cursor:
    print(row)

cnxn.commit()
cnxn.close()