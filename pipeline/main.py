import logging
from extract import extract
from transform import transform
from load import load

# -------------------------
# LOGGING CONFIG
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_pipeline():
    logging.info("Pipeline started")

    df = extract()
    transformed_df = transform(df)
    load(transformed_df)

    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    run_pipeline()
