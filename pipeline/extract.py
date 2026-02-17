import pandas as pd
import logging
import os

def extract(config):
    try:
        csv_path = config["csv_path"]
        logging.info("Starting data extraction")

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_path} not found")

        df = pd.read_csv(csv_path)

        if df.empty:
            raise ValueError("Extracted data is empty")

        logging.info(f"Extracted {len(df)} records")
        return df

    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise
