FROM python:3.10-alpine3.17

WORKDIR /srv

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install flask

COPY requirements.txt /srv/requirements.txt

RUN pip install -r requirements.txt

COPY . /srv

ENV FLASK_APP=run.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8889"]