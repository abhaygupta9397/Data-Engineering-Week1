import logging

def transform(df):
    try:
        logging.info("Starting data transformation")

        df = df.dropna()
        if df.empty:
            raise ValueError("Data empty after cleaning")

        result = df.groupby("city")["amount"].sum().reset_index()
        logging.info("Transformation completed")

        return result

    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        raise
