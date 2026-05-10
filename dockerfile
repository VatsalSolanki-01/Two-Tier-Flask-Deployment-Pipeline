FROM ubuntu 

RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3-flask
RUN pip3 install mysql-connector-python --break-system-packages

COPY . /opt/

EXPOSE 5000

CMD [ "python3", "/opt/app.py" ]

