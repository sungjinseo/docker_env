from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator


with DAG(
    dag_id='train_pet_disease',
    default_args={
        'retries': 0
    },
    schedule='0 0 * * *',
    start_date=datetime(2023, 9, 11),
    #template_searchpath='/usr/local/airflow/include',
    template_searchpath=['/opt/airflow/dags'],
    # 위 경로에서 실행할 script를 찾습니다.
    catchup=False
) as dag_1:

    notebook_task = PapermillOperator(
        task_id="run_training_dog_eye_disease",
        input_nb="/opt/airflow/dags/petmodel/1-1_강아지_눈병_학습_resnet_torch.ipynb",
        output_nb="/opt/airflow/dags/petmodel/out-papermill.ipynb",
        #parameters={"execution_date": "{{ execution_date }}"},
    )