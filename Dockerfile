FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt

RUN pip3 install gunicorn

RUN chmod a+x /app/entrypoint.sh
