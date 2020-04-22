kubectl create configmap statsd-mapping-config --from-file=statsd-mapping.conf=config/statsd-mapping.conf


To install a package from source and debugging in VS Code:
pip3 install --editable git+https://github.com/jaegertracing/jaeger-client-python.git#egg=jaeger-client
pip3 install --editable git+https://github.com/DataDog/dd-trace-py.git#egg=dd-trace


When changing setup.py of dd-trace to add jaeger-client:
cd ./src/dd-trace
pip install -e .