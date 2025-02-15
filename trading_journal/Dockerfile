FROM python:3.11.11-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app/app.py /code/app/app.py

CMD ["python", "app.py", "--host", "0.0.0.0", "port", "81"]