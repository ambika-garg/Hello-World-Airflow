from airflow_operators.sampleOperator import SampleOperator
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "install_private_package_as_requirement",
    description="A simple tutorial DAG",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["requirement"],
) as dag:

    list_requirements = BashOperator(
        task_id="list_requirements",
        bash_command = "pip list"
    )

    test_installed_package = SampleOperator(task_id="test_installed_package", name="foo_bar")

    list_requirements >> test_installed_package