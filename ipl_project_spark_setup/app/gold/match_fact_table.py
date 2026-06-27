from pyspark.sql.functions import *
from config.paths import MATCH_FACT_TABLE_PATH
from utils.logger import get_logger

logger = get_logger(__name__)


def create_match_fact_table(final_silver_df):

    try:

        logger.info("Creating Match Fact Table")

        match_fact_df = (
            final_silver_df
            .groupBy(
                "match_id",
                "season_year",
                "venue_name",
                "team_batting",
                "team_bowling"
            )
            .agg(
                sum("runs_scored").alias("total_runs"),
                sum("extra_runs").alias("extras"),
                count("*").alias("balls"),
                sum(
                    when(col("is_wicket")==1,1)
                    .otherwise(0)
                ).alias("wickets")
            )
        )

        logger.info("Writing Match Fact Table")

        (
            match_fact_df
            .write
            .mode("overwrite")
            .parquet(MATCH_FACT_TABLE_PATH)
        )

        logger.info("Match Fact Table Completed")

        return match_fact_df

    except Exception as e:

        logger.error(f"Error creating Match Fact Table: {e}")

        raise