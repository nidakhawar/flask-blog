FROM python:3.5

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

COPY . .
RUN pip3 install -r requirements.txt
ENV SECRET_KEY="jef676HD"
ENV DATABASE_URI="mysql+pymysql://root:Bismillah@34.89.44.207/flask"
EXPOSE 5000
ENTRYPOINT ["usr/local/bin/python3" , "app.py"]

