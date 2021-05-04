#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 19:45
# @Author  : russell
# @File    : custom_collector.py


from prometheus_client import CollectorRegistry, generate_latest
from flask import Flask, Response
from custom_collector import HostCollector, DockerCollector

app = Flask(__name__)


@app.route('/')
def hello():
    return "test"


@app.route('/metrics/host')
def host():
    host_registry = CollectorRegistry()
    host_registry.register(HostCollector())
    data = generate_latest(host_registry)
    return Response(data, mimetype='text/plain')


@app.route('/metrics/docker')
def docker():
    docker_registry = CollectorRegistry()
    docker_registry.register(DockerCollector())
    data = generate_latest(docker_registry)
    return Response(data, mimetype='text/plain')


if __name__ == '__main__':
    # REGISTRY.register(HostCollector())
    app.run(host='0.0.0.0', port=9100, debug=True)
