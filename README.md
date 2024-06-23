# Basic ETL with Airflow on Codespaces
## Description
In this project, I created and executed two basic ETL DAGS using Airflow on Github Codespaces. The first pipeline is to check the normal functioning of airflow on codespaces as well as scheduler permissions. One thing to not to run airflow on github, disable CSRF in the webserver config file. While restarting the codespace and running the server again github automatically turn CSRF as True and must be disabled again for proper functioning.
In the 2nd DAG, the pipeline performs ETL on a test tree csv file and performs tranformation using python operator and pandas as well as loads the transformed data to Sqlite database. Running on Github codespaces still has pending issues and I would suggest to try Airflow locally.

## Learning Objectives

1. **Orchestration in Data Engineering and Data Pipelines:**  
2. **Installation and Configuration of Airflow on Codespaces:**
3. **Building ETL DAGs in Airflow:** 

### Prerequisites

- Python 3.x
- Apache Airflow (2.6.3)
- SQlite database
- Additional Python libraries (if needed)
