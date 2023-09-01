FROM continuumio/miniconda3
 
#LABEL maintainer="sungjin <*****@gmail.com>"
#LABEL version="0.1"
#LABEL description="Debugging Jupyter Lab"

#작업할 폴더 설정 
WORKDIR /home/jupyter
#WORKDIR /workdir
#COPY . .


# 카카오 ubuntu archive mirror server 추가. 다운로드 속도 향상
RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list && \
    apt-get update

# basic
# linux에서 필요한 기본 프로그램은 여기서 설치
# g++ 설치는 timeout 카카오서버말고 일반서버는 된다
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
	iputils-ping git net-tools ffmpeg\
    wget \
    build-essential \
    libboost-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    g++ \
    gcc \
    curl \
    bzip2 \
    ca-certificates \
	libgl1-mesa-glx \
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

#RUN apt install -y --no-install-recommends \
#    gcc nano wget iputils-ping git net-tools curl zip unzip ffmpeg fontconfig build-essential

# 아나콘다에서 사용할 모듈을 설치
#RUN chmod 755 /etc/profile.d/conda.sh
#RUN . /etc/profile.d/conda.sh
RUN echo "conda activate base" >> ~/.bashrc

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

#RUN pip install matplotlib
#RUN pip install -r /workdir/requirements.txt

# 나눔고딕 폰트 설치, D2Coding 폰트 설치
# matplotlib에 Nanum 폰트 추가
#RUN apt-get install fonts-nanum* && \
#    mkdir -p ~/.local/share/fonts && \
#    cd ~/.local/share/fonts && \
#    wget https://github.com/naver/d2codingfont/releases/download/VER1.3.2/D2Coding-Ver1.3.2-20180524.zip && \
#    unzip D2Coding-Ver1.3.2-20180524.zip && \
#    mkdir /usr/share/fonts/truetype/D2Coding && \
#    cp ./D2Coding/*.ttf /usr/share/fonts/truetype/D2Coding/ && \
#    #cp /usr/share/fonts/truetype/nanum/Nanum* /opt/conda/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf/ && \
#    fc-cache -fv && \
#    rm -rf D2Coding* && \
#    rm -rf ~/.cache/matplotlib/*
	

RUN apt-get update && apt-get install -y vim locales tzdata && \
    locale-gen ko_KR.UTF-8 && locale -a && \
    ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# LANG 환경변수 설정
ENV LANG ko_KR.UTF-8

RUN conda install -c conda-forge jupyterlab	
RUN conda install -c conda-forge nodejs
#RUN jupyter labextension install @jupyterlab/debugger
#RUN conda install xeus-python -c conda-forge
#RUN conda install -c conda-forge xeus-python

RUN jupyter lab --generate-config

#USER greatseo
 
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
