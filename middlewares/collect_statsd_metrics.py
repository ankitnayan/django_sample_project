import django
import time
from datadog import DogStatsd


if django.VERSION >= (1, 10, 0):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object


statsd = DogStatsd(host="localhost", port=9125)

REQUEST_LATENCY_METRIC_NAME = 'django_request_latency_seconds'
REQUEST_COUNT_METRIC_NAME = 'django_request_count'


class StatsdMetricsMiddleware(MiddlewareMixin):

    def process_request(self, request):

        request.start_time = time.time()
        

    def process_response(self, request, response):

        statsd.increment(REQUEST_COUNT_METRIC_NAME,
            tags=[
                'service:django_sample_project', 
                'method:%s' % request.method, 
                'endpoint:%s' % request.path,
                'status:%s' % str(response.status_code)
                ]
        )

        resp_time = (time.time() - request.start_time)*1000
        
        #print(resp_time)

        statsd.histogram(REQUEST_LATENCY_METRIC_NAME,
                resp_time,
                tags=[
                    'service:django_sample_project',
                    'endpoint:%s' % request.path,
                    ]
        )

        return response

