FROM python:3.7

COPY . /app

 

RUN pip install tensorflow

ADD requirements.txt /app/

RUN pip install -r /app/requirements.txt 

ADD example.py /app/

CMD ["python3", "/app/example.py"]




