import django
import time
from datadog import DogStatsd


if django.VERSION >= (1, 10, 0):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object


statsd = DogStatsd(host="localhost", port=9125)

REQUEST_LATENCY_METRIC_NAME = 'request_latency_seconds'
REQUEST_COUNT_METRIC_NAME = 'request_count'


class StatsdMetricsMiddleware(MiddlewareMixin):

    def process_request(self, request):

        #request.prometheus_before_middleware_event = time.time()
        print("I am before all middlewares")


    def process_response(self, request, response):

        statsd.increment(REQUEST_COUNT_METRIC_NAME,
            tags=[
                'service:django_sample_project', 
                'method:%s' % request.method, 
                'endpoint:%s' % request.path,
                'status:%s' % str(response.status_code)
                ]
        )
        print("I am after all middlewares")
        return response

