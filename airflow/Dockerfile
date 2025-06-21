FROM apache/airflow:3.0.2-python3.12
# копируем файл в целевую директорию
COPY requirements.txt ./tmp/requirements.txt
RUN pip install -U pip
RUN pip install -r ./tmp/requirements.txt 