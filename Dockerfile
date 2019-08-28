FROM python:3.7.3
MAINTAINER ankitnayan
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn django_sample_project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile='-' --statsd-host=localhost:9125 --access-logformat='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(p)s"'