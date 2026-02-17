import sqlite3
import logging

DB_PATH = "sales.db"
TABLE_NAME = "city_sales"

def load(df):
    try:
        logging.info("Starting data load")

        conn = sqlite3.connect(DB_PATH)
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
        conn.close()

        logging.info("Data loaded successfully")

    except Exception as e:
        logging.error(f"Load failed: {e}")
        raise
