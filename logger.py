#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 19:45
# @Author  : russell
# @File    : host.py


import logging


def get_logger(name: str, level_int: int, formatter_str: str, log_path: str, stream=True):
    logger = logging.getLogger(name)
    # level
    logger.setLevel(level=level_int)
    # Formatter
    formatter = logging.Formatter(formatter_str)
    # FileHandler
    if log_path:
        fh = logging.FileHandler(log_path)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # StreamHandler
    # if stream:
    #     sh = logging.StreamHandler()
    #     sh.setFormatter(formatter)
    #     logger.addHandler(sh)

    return logger
