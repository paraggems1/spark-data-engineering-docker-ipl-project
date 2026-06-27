# IPL Data Engineering Pipeline using PySpark and Docker

## Author: Parag Sonawane
[This project was designed and implemented from scratch as a personal Data Engineering learning and portfolio project using publicly available IPL datasets.]

## YouTube Walkthrough: Coming Soon


## Project Overview

This project was built to simulate a practical end-to-end Data Engineering workflow using IPL cricket datasets.

The goal was not only to perform analytics on IPL data, but also to design a pipeline that resembles how batch data processing systems are commonly organized in production environments.

The project follows a Medallion Architecture approach:


Raw Data -> Bronze -> Silver -> Gold -> Analytics


using PySpark running inside Docker containers.

---

## Problem Statement

IPL datasets are available as multiple CSV files representing matches, deliveries, players, teams and venues.

To perform meaningful analytics, the data first needs to be:

* Ingested
* Validated
* Standardized
* Joined
* Enriched
* Aggregated

This project demonstrates that complete journey.

---
## DataSet Source Details: 
## IPL Dtaset:
https://data.world/raghu543/ipl-data-till-2017

Ball By Ball Data of all the IPL seasons (637 matches including 2017) A Complete datawarehouse

## Architecture

## High Level Architecture Diagram 
![Architecture Diagram](docs/Architecture/Architecture_Diagram.png)

```
                    IPL CSV Files
                           |
                           v

+--------------------------------------------------+
|                    RAW LAYER                     |
|--------------------------------------------------|
| Match.csv                                        |
| Ball_By_Ball.csv                                 |
| Player.csv                                       |
| Team.csv                                         |
| Venue.csv                                        |
+--------------------------------------------------+

                           |
                           v

+--------------------------------------------------+
|                  BRONZE LAYER                    |
|--------------------------------------------------|
| Data ingestion                                   |
| Schema validation                                |
| Initial cleansing                                |
| Parquet conversion                               |
+--------------------------------------------------+

                           |
                           v

+--------------------------------------------------+
|                  SILVER LAYER                    |
|--------------------------------------------------|
| Dataset joins                                    |
| Business transformations                         |
| Feature engineering                              |
| Analytical dataset preparation                   |
+--------------------------------------------------+

                           |
                           v

+--------------------------------------------------+
|                   GOLD LAYER                     |
|--------------------------------------------------|
| Match Fact Table                                 |                                  |
| Aggregated KPIs                                  |
| Analytical outputs                               |
+--------------------------------------------------+

                           |
                           v

+--------------------------------------------------+
|                   ANALYTICS                      |
|--------------------------------------------------|
| Spark SQL                                        |
| Pandas Analysis                                  |
| Matplotlib Visualizations                        |
| Business Insights                                |
+--------------------------------------------------+
```

---

## Technology Stack

| Component            | Technology |
| -------------------- | ---------- |
| Language             | Python     |
| Processing Engine    | PySpark    |
| Query Engine         | Spark SQL  |
| Containerization     | Docker     |
| Analytics            | Pandas     |
| Visualization        | Matplotlib |
| Storage Format       | Parquet    |
| Notebook Environment | Jupyter    |

---

## Repository Structure

## Project Folder Structure 

![Project Structure](Docs/Screenshots/01.png)


![Project Structure](Docs/Screenshots/01.png)

## Docker Environment

![Docker Desktop](Docs/Screenshots/02-Docker-Desktop.png)

![Docker Compose Configuration](Docs/Screenshots/18-Docker-Comose_yaml_file.png)

![Dockerfile](Docs/Screenshots/19-Dockerfile.png)

![Docker Spark Linux Server](Docs/Screenshots/17-Docker_Spark_Linux_Server.png)

```
IPL_DATAENGG_DOCKER_PROJECT_SETUP
│
├── data/
│   ├── 1-raw/
│   │   ├── Ball_By_Ball.csv
│   │   ├── Match.csv
│   │   ├── Player.csv
│   │   ├── Player_match.csv
│   │   └── Team.csv
│   │
│   ├── 2_bronze/
│   │   ├── ball_by_ball_parquet/
│   │   ├── match_parquet/
│   │   ├── player_parquet/
│   │   ├── player_match_parquet/
│   │   └── team_parquet/
│   │
│   ├── 3_silver/
│   │   ├── ball_by_ball_parquet/
│   │   ├── match_parquet/
│   │   ├── player_parquet/
│   │   ├── player_match_parquet/
│   │   ├── team_parquet/
│   │   └── final_silver_parquet/
│   │
│   └── 4_gold/
│       ├── match_fact_table/
│       ├── batting_summary/
│       ├── bowling_summary/
│       ├── orange_cap/
│       ├── team_performance/
│       ├── venue_analysis/
│       └── death_over_analysis/
│
├── notebooks
│   │
│   ├── 01_ipl_data_ingestion.ipynb
│   ├── 02_ipl_data_validate_write_bronze.ipynb
│   ├── 03_ipl_data_transform_silver.ipynb
│   ├── 04_ipl_data_transformation_gold.ipynb
│   └── 05_spark_sql_analytic.ipynb
│
├── app
│   │
│   ├── config
│   │   └── paths.py
│   │
│   ├── utils
│   │   └── logger.py
│   │
│   ├── gold
│   │   ├── match_fact_table.py
│   │   └── batting_summary.py
│   │
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Pipeline Flow

## 1. Data Ingestion

## Notebook Based Development Workflow 
![Notebook 1](Docs/Screenshots/03-Notebook1.png) 
![All Notebooks](Docs/Screenshots/04-All-Notebooks.png) 
![Notebook 2](Docs/Screenshots/05-Notebook2.png) 
![Notebook 3](Docs/Screenshots/06-Notebook3.png) 
![Notebook 4](Docs/Screenshots/07-Notebook4.png)

## Raw Dataset 
![Raw CSV Files](Docs/Screenshots/12-Raw-files-csv.png)

Raw IPL CSV files are loaded into Spark DataFrames.

---

## 2. Bronze Layer

## Spark Session Initialization 
![Spark Session](Docs/Screenshots/08-Spark-Session.png)

* Schema validation
* Data quality checks
* Conversion to parquet format

The bronze layer acts as the first persistent storage layer.

---

## 3. Silver Layer

The silver layer combines multiple IPL datasets and applies business logic transformations.

Examples:

* Match enrichment
* Team information joins
* Venue enrichment
* Feature generation

This layer becomes the primary analytical dataset for downstream processing.

---

## 4. Gold Layer

## Match Fact Table Generated 
![Match Fact Table](Docs/Screenshots/13-Match_fact-Table_Parquet-formed.png) 

### Gold Layer Outputs 
![Gold Layer Tables](Docs/Screenshots/15-Gold_Layer_Tables_Formed.png)

🏆 Gold Layer (Business-Facing Analytical Products)
├── 📊 match_fact_table
├── 🏏 batting_summary
├── 🥎 bowling_summary
├── 👑 orange_cap
├── 👥 team_performance
├── 🏟️ venue_analysis
└── ⚡ death_over_analysis

Current implementation includes modular transformations of two following tables:

* Match Fact Table
* Batting Summary Table

These tables are designed to support reporting and analytical use cases.

---

## 5. Analytics Layer

## Spark SQL Analytics 
![Spark SQL DataFrame](Docs/Screenshots/20-UI-Spark-SQL-Dataframe-.png)

## Top Performing Bowlers 
![Top Bowlers](Docs/Screenshots/09-TopTenBowlers.png) 

### Top Run Scorers 
![Top Run Scorers](Docs/Screenshots/10-TopTenRunScorer.png)

The final stage focuses on extracting insights using:

* Spark SQL
* Pandas
* Matplotlib

Examples include:

* Team performance analysis
* Venue analysis
* Batting trends
* Match statistics

---

## Production Practices Included

Although this project is intended primarily for demonstration purposes, several production-oriented concepts have been incorporated:

* Modular transformations
* Centralized path configuration
* Logging
* Exception handling
* Reusable transformation functions
* Dockerized execution environment
* Parquet-based storage strategy

The modular design demonstrated in selected Gold layer components can be extended further across additional tables and pipeline stages when required.

---

## Example Execution Logs

## Pipeline Execution 
![Pipeline Start](Docs/Screenshots/11-Terminal-Before.png)
![Pipeline Logs](Docs/Screenshots/14-Terminal_Logs_After_Spark_Session_Successful_Run.png) 
![Pipeline Completion](Docs/Screenshots/16-Terminal-Thank-You.png)

```text
INFO Reading Silver Dataset

INFO Creating Match Fact Table
INFO Writing Match Fact Table
INFO Match Fact Table Completed

INFO Creating Batting Summary
INFO Writing Batting Summary
INFO Batting Summary Completed
```

---

## Running the Project

Start containers:

```bash
docker compose up -d
```

Open container:

```bash
docker exec -it spark-master bash
```

Execute pipeline:

```bash
python /opt/spark-app/main.py
```

or

```bash
spark-submit /opt/spark-app/main.py
```

---

## Spark UI Monitoring

## Completed Jobs

![Spark Completed Jobs](Docs/Screenshots/21-UI-Spark-Completed-Jobs.png)

#### Completed Stages

![Spark Completed Stages](Docs/Screenshots/22-UI-Spark-Completed-Stages.png)


---

## Possible Future Enhancements

* Airflow orchestration
* Incremental processing
* Cloud storage integration
* Data quality framework
* CI/CD integration
* Monitoring and alerting

---

## Closing Notes

The objective of this project was to build a practical end-to-end Spark pipeline while keeping the implementation approachable and easy.

The focus was on understanding the complete lifecycle of data movement and transformation rather than optimizing for framework complexity.

This project serves as a foundation that can be extended into larger production-grade workflows as requirements evolve.


## * Video walkthrough with voice-over explanation (coming soon)
