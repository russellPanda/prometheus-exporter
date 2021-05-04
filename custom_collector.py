#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 19:45
# @Author  : russell
# @File    : custom_collector.py

import logging
from prometheus_client.core import GaugeMetricFamily

from mes.host import Host
from mes.docker import HostDocker
from logger import get_logger

# setting logging

format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
collect_logger = get_logger("collect_logger", logging.DEBUG, format_str, 'collector.log')


class HostCollector(object):
    def __init__(self):
        pass

    def collect(self):
        """ 收集主机信息到指标"""

        local_host = Host()

        cpu_use_metric = GaugeMetricFamily("cpu_Usage", 'psutil cpu percent', labels=['cpu_number'])
        for mes in local_host.cpu_percent_per():
            cpu_use_metric.add_metric([str(mes.number)], mes.percent)
        collect_logger.info("get cpu percent metric...")
        yield cpu_use_metric


class DockerCollector(object):
    def __init__(self):
        pass

    def collect(self):
        """ 收集主机信息到指标"""

        local_docker = HostDocker()
        docker_metric = GaugeMetricFamily("docker_cpu", 'docker container cpu percent',
                                          labels=['id', 'image', 'status'])
        for mes in local_docker.containers_mes():
            docker_metric.add_metric([mes.id, mes.image, mes.status], mes.cpu_per)
        collect_logger.info("get docker cpu percent metric ...")
        yield docker_metric
