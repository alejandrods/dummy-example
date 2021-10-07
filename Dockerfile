# Dockerfile
FROM python:3.8

WORKDIR = .

EXPOSE 8080

COPY /src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD ./src ./

ENTRYPOINT ["python", "app.py"]
