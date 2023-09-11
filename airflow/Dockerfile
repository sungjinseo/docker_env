FROM apache/airflow:2.7.0
COPY requirement.txt .   
RUN pip install -r requirement.txt
RUN pip install --upgrade pip ipython ipykernel   
RUN ipython kernel install --name "python3" --user
CMD python -m ipykernel_launcher -f $DOCKERNEL_CONNECTION_FILE
