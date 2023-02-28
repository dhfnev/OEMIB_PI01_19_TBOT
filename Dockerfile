FROM python:3.10.7-bullseye
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
COPY config/ .
COPY res/ .
CMD [ "python", "./app.py" ]