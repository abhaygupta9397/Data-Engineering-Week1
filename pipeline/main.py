import logging
from extract import extract
from transform import transform
from load import load
from config import load_config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_pipeline():
    logging.info("Pipeline started")

    config = load_config()

    df = extract(config)
    df = transform(df)
    load(df, config)

    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    run_pipeline()
