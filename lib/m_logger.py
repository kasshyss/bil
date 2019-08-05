#-*- coding: utf-8 -*-
# *********************************************
# Purpose : manage logger
# Author : Meriadoc
# Log : 
#     * 24/07/2019 : PB : Init
# *********************************************

import logging
import inspect

def get_logger(name, level):

    logger_formatter = '%(asctime)s | %(levelname)s | %(name)s.%(funcName)s : %(message)s'

    if level not in (10,20,30,40,50):
        return False

    if not isinstance(name, str):
        return False

    logger = logging.getLogger(name)
    logger.setLevel(level)

    sh = logging.StreamHandler()
    formatter = logging.Formatter(logger_formatter)

    sh.setLevel(level)
    sh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.propagate = False

    logger.debug('{} : Logger created'.format(inspect.stack()[0][3]))

    return logger

def get_logger_level(level):

    if level == 'debug':
        return logging.DEBUG
    elif level == 'warning':
        return logging.WARNING
    elif level == 'error':
        return logging.ERROR
    else:
        return logging.INFO
