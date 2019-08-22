FROM python:3.7.3
MAINTAINER ankitnayan
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn django_sample_project.wsgi:application --bind localhost:8000 --workers 3 --statsd-host=localhost:9125 --statsd-prefix=sample_project
