FROM python:3.9

WORKDIR /app

COPY app.py .

RUN pip install flask flask-cors mysql-connector-python

CMD ["python", "app.py"]
