import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM city_sales where amount > 250", conn)
print(df)
conn.close()
