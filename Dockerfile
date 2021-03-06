FROM python:3
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /concord/
RUN pip install -r /concord/requirements.txt

WORKDIR /concord/
CMD python3 manage.py runserver 0.0.0.0:8000
