# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]
