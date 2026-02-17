import sqlite3
import logging

def load(df, config):
    try:
        db_path = config["db_path"]
        table = config["table_name"]

        logging.info("Starting data load")

        conn = sqlite3.connect(db_path)
        df.to_sql(table, conn, if_exists="replace", index=False)
        conn.close()

        logging.info("Data loaded successfully")

    except Exception as e:
        logging.error(f"Load failed: {e}")
        raise
