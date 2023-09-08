from datetime import datetime, date, timedelta
import pandas as pd
from io import BytesIO
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from minio import Minio
from sqlalchemy.engine import create_engine

MINIO_BUCKET_NAME = 'etl'
MINIO_ADDRESS =  '221.138.17.149:5002'
MINIO_ROOT_USER = 'TB6ZsnwHliJYom97'
MINIO_ROOT_PASSWORD = 'pKkoKZVJhbvOeW21kcm7U6ybuuP7TKp2'


DEFAULT_ARGS = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 5),
}

dag = DAG('etl_department_salary_left_att',
          default_args=DEFAULT_ARGS,
          schedule_interval="@once"
          )

data_lake_server = Variable.get("data_lake_server")
data_lake_login = Variable.get("data_lake_login")
data_lake_password = Variable.get("data_lake_password")
data_lake_bucket = 'etl'

database_server = Variable.get("database_server")
database_login = Variable.get("database_login")
database_password = Variable.get("database_password")
database_name = Variable.get("database_name")

url_connection = "mysql+pymysql://{}:{}@{}/{}".format(
                 str(database_login), str(database_password), str(database_server), str(database_name)
)

engine = create_engine(url_connection)

client = Minio(
    data_lake_server,
    access_key=data_lake_login,
    secret_key=data_lake_password,
    secure=False
)

def extract():

    # query para consultar os dados.
    query = """
            SELECT emp.lastName, emp.firstName
              FROM employees emp;
            """

    df_ = pd.read_sql_query(query, engine)

    # persiste os arquivos na área de Staging.
    df_.to_csv("/tmp/department_salary_left.csv", index=False)

def load():
    # carrega os dados a partir da área de staging.
    df_ = pd.read_csv("/tmp/department_salary_left.csv")


    # converte os dados para o formato parquet.
    df_.to_parquet(
        "/tmp/department_salary_left.parquet", index=False
    )

    # carrega os dados para o Data Lake.
    client.fput_object(
        data_lake_bucket,
        "department_salary_left.parquet",
        "/tmp/department_salary_left.parquet"
    )
    
    #minioClient.fput_object(bucket, upload_path + file_name, upload_file)


extract_task = PythonOperator(
    task_id='extract_data_from_database',
    provide_context=True,
    python_callable=extract,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_file_to_data_lake',
    provide_context=True,
    python_callable=load,
    dag=dag
)

clean_task = BashOperator(
    task_id="clean_files_on_staging",
    bash_command="rm -f /tmp/*.csv;rm -f /tmp/*.json;rm -f /tmp/*.parquet;",
    dag=dag
)

extract_task >> load_task >> clean_task