''' Basic ETL DAG'''
from datetime import datetime, date
import pandas as pd
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG

with DAG(
    dag_id='basic_etl_dag',
    schedule_interval=None,
    start_date=datetime(2024, 6, 23),
    catchup=False) as dag:

    # The location of the top-level-domain-names.csv file has changed. Now, it is hosted in the same repository as this project.
    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='echo "......Trees data is extracted to the ecosystem"'
        )

    def transform_data():
        """Read in the file, and write a transformed file out"""
        today = date.today()
        print("Todays's date:",today.date())

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag)

    load_task = BashOperator(
        task_id='load_task',
        bash_command='echo "Loaded"',
        dag=dag)

    extract_task >> transform_task >> load_task