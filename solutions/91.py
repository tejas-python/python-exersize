# csv to db
import sqlite3
import pandas as pd

df = pd.read_csv('ten_more_countries.txt')




conn = sqlite3.connect('database.db')
curr = conn.cursor()
for i in range(0,len(df)):
    l = list(df.loc[i])
    # print(l)
    curr.execute("INSERT INTO countries (ID,Country,Area,Population) values(NULL,?,?,NULL)",(l[1],l[2]))

conn.commit()
conn.close()
print("done")
