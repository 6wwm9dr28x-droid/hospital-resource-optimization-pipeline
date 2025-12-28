"""
Hospital Resource Optimization Pipeline DAG

Conceptual Apache Airflow DAG demonstrating orchestration of the
hospital data engineering pipeline. This DAG is not executed as part
of the submission but reflects correct pipeline dependencies.
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "student",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="hospital_resource_optimization_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Conceptual DAG for hospital data pipeline",
) as dag:

    ingest_appointment_data = BashOperator(
        task_id="ingest_appointment_data",
        bash_command="python src/data_ingestion/convert_xlsx_to_csv.py",
    )

    ingest_hdhi_data = BashOperator(
        task_id="ingest_hdhi_admissions_data",
        bash_command="python src/data_ingestion/load_hdhi_data.py",
    )

    clean_appointment_data = BashOperator(
        task_id="clean_appointment_data",
        bash_command="python src/data_cleaning/clean_hospital_data.py",
    )

    clean_hdhi_data = BashOperator(
        task_id="clean_hdhi_data",
        bash_command="python src/data_cleaning/clean_hdhi_data.py",
    )

    feature_engineering = BashOperator(
        task_id="feature_engineering_los",
        bash_command="echo 'LOS feature generated during cleaning'",
    )

    analytics_reporting = BashOperator(
        task_id="analytics_and_reporting",
        bash_command="echo 'Tables and figures generated from evaluation scripts'",
    )

    ingest_appointment_data >> clean_appointment_data
    ingest_hdhi_data >> clean_hdhi_data
    clean_hdhi_data >> feature_engineering
    [clean_appointment_data, feature_engineering] >> analytics_reporting
