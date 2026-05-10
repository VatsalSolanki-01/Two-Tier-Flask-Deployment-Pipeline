FROM ubuntu 

RUN apt-get update
RUN apt-get install -y python3 
RUN apt install -y python3-pip
RUN apt-get install -y python3-flask
RUN pip install mysql-connector-python --break-system-packages

COPY . /opt/

EXPOSE 5000

CMD [ "python3", "/opt/app.py" ]

