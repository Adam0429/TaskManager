FROM ubuntu
COPY . /TaskManager
WORKDIR /TaskManager
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 8000

