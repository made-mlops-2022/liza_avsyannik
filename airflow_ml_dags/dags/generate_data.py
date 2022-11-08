from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


LOCAL_DATA_DIR = Variable.get('local_data_dir')

default_args = {
    'owner': 'airflow',
    'email': ['airflow@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'generate_data',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(14),  # TODO
) as dag:
    generate = DockerOperator(
        image='airflow-generate-data',
        command="--output-dir /data/raw/",
        network_mode='bridge',
        task_id='docker-airflow-generate-data',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    generate
