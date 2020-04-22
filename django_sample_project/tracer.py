from jaeger_client import Config

config = Config(
    config={ # usually read from some yaml config
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name='jaeger-django-project',
    validate=True,
)
# this call also sets opentracing.tracer

tracer = None


def get_tracer():
    from ddtrace import patch_all; patch_all(logging=True)
    
    global tracer
    if not tracer:
        tracer = config.initialize_tracer()
        print ("tracer initialised ...")

    return tracer

