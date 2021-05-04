#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 19:45
# @Author  : russell
# @File    : custom_collector.py

# https://docs.docker.com/engine/api/v1.41/#operation/ContainerStats

from collections import namedtuple
import docker
from docker.models.containers import Container


class HostDocker:
    def __init__(self) -> None:
        self.client = docker.from_env()

    def all_containers(self):
        return self.client.containers.list()

    def get_container(self, container_id: str):
        return self.client.containers.get(container_id)

    @classmethod
    def container_id(cls, con: Container) -> str:
        return con.id

    @classmethod
    def container_image(cls, con: Container) -> str:
        return con.image.tags[0]

    @classmethod
    def container_status(cls, con: Container) -> str:
        con.reload()
        return con.attrs['State']['Status']

    @classmethod
    def container_cpu_percent(cls, con: Container) -> float:
        stats_dict = con.stats(stream=False)
        cpu_delta = stats_dict['cpu_stats']['cpu_usage']['total_usage'] - stats_dict['precpu_stats']['cpu_usage'][
            'total_usage']
        system_cpu_delta = stats_dict['cpu_stats']['system_cpu_usage'] - stats_dict['precpu_stats']['system_cpu_usage']
        number_cpus = stats_dict['cpu_stats']['online_cpus']
        return (cpu_delta / system_cpu_delta) * number_cpus * 100.0

    def containers_mes(self) -> list:
        ConMes = namedtuple('container_mes', ['id', 'image', 'status', 'cpu_per'])
        cons = self.all_containers()
        mes = list()
        for con in cons:
            id = HostDocker.container_id(con)
            image = HostDocker.container_image(con)
            status = HostDocker.container_status(con)
            cpu_per = HostDocker.container_cpu_percent(con)
            mes.append(ConMes(id, image, status, cpu_per))
        return mes


if __name__ == '__main__':
    local = HostDocker()
    print(local.containers_mes())