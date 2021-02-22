import pyodbc
import pandas as pd
import numpy as np



cnxn = pyodbc.connect("DRIVER={ODBC 5.1 Driver};SERVER=;PORT=;DATABASE=;USER=;PASSWORD=;")


excel = pd.read_excel(r'C:\Users\andri\Desktop\PW\Data\organization.xlsx')



def LoadData(data):
    for index, row in data.iterrows():
       
        sql = "INSERT organization(Name,Address,Email,Passwords,Phone_number) VALUES ('{}', '{}', '{}', '{}','{}')".format(row["Name"],row["Address"],row["Email"],row["Passwords"],row["Phone_number"])
        cursor.execute(sql)

LoadData(excel)

cursor.execute("SELECT * FROM organization")
for row in cursor:
    print(row)

conn.commit()
conn.close()