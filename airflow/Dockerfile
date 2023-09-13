FROM apache/airflow:2.7.0

COPY requirement.txt .   

RUN pip install -r requirement.txt
RUN pip install --upgrade pip ipython ipykernel   
RUN ipython kernel install --name "python3" --user
CMD python -m ipykernel_launcher -f $DOCKERNEL_CONNECTION_FILE

USER root
RUN apt-get update && \
    apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey
RUN apt-key add /tmp/dkey && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable"
RUN apt-get update && \
    apt-get -y install docker-ce

RUN /bin/bash -c groupadd --gid 1001
RUN usermod -aG docker 'airflow'

USER airflow

