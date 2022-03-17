# connect to data base SELECT countries table get countries whose area>200000:


import sqlite3
conn = sqlite3.connect('database.db')
curr = conn.cursor()
curr.execute("SELECT Country FROM countries where area >2000000")
rows = curr.fetchall()
conn.close()

for i in rows:
    print(i[0])
