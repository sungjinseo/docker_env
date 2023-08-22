#FROM debian:bookworm-slim
FROM continuumio/miniconda3
LABEL maintainer="greatseo <sjseo85@gmail.com>"
LABEL description="jupuyter lab for codingtest"

ENV PATH /opt/conda/envs/py39/bin:$PATH
ENV CONDA_DEFAULT_ENV py39
ENV CONDA_PREFIX /opt/conda/envs/py39
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    wget \
    build-essential \
    libboost-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    g++ \
    gcc \
    python3-dev \
    python3-pip \
    curl \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    libssl-dev \
    libzmq3-dev \
    vim \
    git &&\
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*


COPY environment.yml .
RUN conda env create -f environment.yml

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate py39" >> ~/.bashrc


COPY requirements.txt .
RUN pip install -r requirements.txt

RUN jupyter contrib nbextension install --user && \
    jupyter nbextension enable varInspector/main

RUN jupyter nbextension install --overwrite --py nbtutor &&\
    jupyter nbextension enable --py nbtutor

#JAVA kernel
RUN apt-get update || true
RUN apt-get install -y openjdk-17-jdk-headless git
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8
RUN apt-get install -y curl

RUN git clone https://github.com/frankfliu/IJava.git
RUN cd IJava/ && ./gradlew installKernel && cd .. && rm -rf IJava/
RUN rm -rf ~/.gradle

WORKDIR /home/jupyter

EXPOSE 8888
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''",  "--NotebookApp.password=''"]