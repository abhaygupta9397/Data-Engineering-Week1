import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM city_sales", conn)
print(df)
conn.close()
