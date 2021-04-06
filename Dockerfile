FROM ubuntu
COPY . /TaskManager
WORKDIR /TaskManager
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN wget https://www.emqx.cn/downloads/broker/v4.2.9/emqx-ubuntu20.04-4.2.9-x86_64.zip
RUN unzip emqx-ubuntu20.04-4.2.9-x86_64.zip
EXPOSE 8000

