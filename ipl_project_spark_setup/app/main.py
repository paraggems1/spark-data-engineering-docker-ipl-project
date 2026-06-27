

from pyspark.sql import SparkSession
from gold.match_fact_table import create_match_fact_table
from gold.batting_summary import create_batting_summary
from config.paths import FINAL_SILVER_PATH
from utils.logger import get_logger

logger = get_logger(__name__)


def create_spark():
    spark = (
        SparkSession.builder
        .appName("IPL_GOLD_LAYER")
        .master("local[*]")
        .config("spark.driver.memory", "4g")
        .getOrCreate()
    )

    return spark


def main():

    spark = None

    try:
        logger.info("Starting Gold Layer Pipeline")

        spark = create_spark()

        logger.info("Reading final silver dataset")
        final_silver_df = spark.read.parquet(
            FINAL_SILVER_PATH
        )

        logger.info("Creating match fact table")
        create_match_fact_table(
            final_silver_df
        )

        logger.info("Creating batting summary")
        create_batting_summary(
            final_silver_df
        )

        logger.info("Gold Layer Pipeline completed successfully")

    except Exception:
        logger.exception(
            "Gold Layer Pipeline failed"
        )
        raise

    finally:
        if spark:
            spark.stop()
            logger.info("Spark Session stopped")


if __name__ == "__main__":
    main()