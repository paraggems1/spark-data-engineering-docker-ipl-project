from pyspark.sql.functions import *
from config.paths import BATTING_SUMMARY_PATH
from utils.logger import get_logger

logger = get_logger(__name__)


def create_batting_summary(final_silver_df):

    try:

        logger.info("Creating batting summary")

        batting_summary_df = (

            final_silver_df

            .groupBy(
                "striker",
                "striker_name"
            )

            .agg(

                sum("runs_scored")
                .alias("total_runs"),

                count("*")
                .alias("balls_faced"),

                sum(
                    when(col("is_four")==1,1)
                    .otherwise(0)
                ).alias("fours"),

                sum(
                    when(col("is_six")==1,1)
                    .otherwise(0)
                ).alias("sixes"),

                countDistinct("match_id")
                .alias("matches")

            )

        )

        batting_summary_df = batting_summary_df.withColumn(

            "strike_rate",

            round(

                (col("total_runs") /
                 col("balls_faced")) * 100,

                2

            )
        )

        logger.info("Writing batting summary")

        (
            batting_summary_df
            .write
            .mode("overwrite")
            .parquet(BATTING_SUMMARY_PATH)
        )

        logger.info("Batting summary completed")

        return batting_summary_df


    except Exception as e:

        logger.error(
            f"Batting Summary Failed : {e}"
        )

        raise

