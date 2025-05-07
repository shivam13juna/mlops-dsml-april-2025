from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import random

def create_text_file():
	# Generate random text
	random_text = "This is some random text."

	# Create a new text file and write the random text to it
	with open("/home/ubuntu/airflow/dags/file.txt", "w") as file:
		file.write(random_text)

dag = DAG(
	'create_text_file_dag',
	description='DAG to create a text file with random text',
	schedule_interval='0 3 * * *',
	start_date=datetime(2022, 1, 1),
)

create_text_file_task = PythonOperator(
	task_id='create_text_file_task',
	python_callable=create_text_file,
	dag=dag,
)

create_text_file_task