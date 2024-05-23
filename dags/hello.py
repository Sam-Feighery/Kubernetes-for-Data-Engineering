from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_augs = {
    'owner': 'SamFeighery',
    'start_date': datetime(2024, 5, 22),
    'catchup': False
}

dag = DAG(
    'hello_world',
    default_args= default_augs,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_Sam',
    bash_command='echo "Hello Sam"',
    dag = dag
)

t1 >> t2