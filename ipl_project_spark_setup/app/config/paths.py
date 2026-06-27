# Silver Layer
SILVER_PATH = "/opt/spark-data/3_silver"

FINAL_SILVER_PATH = (
    f"{SILVER_PATH}/final_silver_parquet"
)


# Gold Layer
GOLD_PATH = "/opt/spark-data/4_gold"

MATCH_FACT_TABLE_PATH = (
    f"{GOLD_PATH}/match_fact_table"
)

BATTING_SUMMARY_PATH = (
    f"{GOLD_PATH}/batting_summary"
)

BOWLING_SUMMARY_PATH = (
    f"{GOLD_PATH}/bowling_summary"
)

DEATH_OVER_ANALYSIS_PATH = (
    f"{GOLD_PATH}/death_over_analysis"
)

ORANGE_CAP_PATH = (
    f"{GOLD_PATH}/orange_cap"
)

TEAM_PERFORMANCE_PATH = (
    f"{GOLD_PATH}/team_performance"
)

VENUE_ANALYSIS_PATH = (
    f"{GOLD_PATH}/venue_analysis"
)