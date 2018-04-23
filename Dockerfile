FROM python:3.6

WORKDIR /usr/src/app

COPY *.py ./

RUN pip install --no-cache-dir confluent-kafka flask gunicorn

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "main:app" ]   