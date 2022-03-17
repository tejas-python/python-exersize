
# db to csv

#
import sqlite3
import pandas as pd
conn = sqlite3.connect('database.db')
curr = conn.cursor()
curr.execute("SELECT * FROM countries where area >2000000")
rows = curr.fetchall()
conn.close()

df = pd.DataFrame.from_records(rows,columns=['Ranks','Country','Area',"Population"])
df.to_csv("con_data.csv",index_label=False)
print("done")
# print(df)
