import pandas as pd
import logging
import os

CSV_PATH = "data/sales.csv"

def extract():
    try:
        logging.info("Starting data extraction")

        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(f"{CSV_PATH} not found")

        df = pd.read_csv(CSV_PATH)

        if df.empty:
            raise ValueError("Extracted data is empty")

        logging.info(f"Extracted {len(df)} records")
        return df

    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise
