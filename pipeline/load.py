import sqlite3

def load(df):
    conn = sqlite3.connect("sales.db")
    df.to_sql("city_sales", conn, if_exists="replace", index=False)
    conn.close()
