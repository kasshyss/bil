#-*- coding: utf-8 -*-

"""
* Purspose : Manage conf files - for any purpose about conf file structure please check python doc.
* Author : Meriadoc
* Log :
    * 05/08/2019 : PB : Initial commit
"""


import m_logger as log
import configparser
import os

logger = log.get_logger('conf', log.get_logger_level('info'))


"""
* Purpose : resturn a dict of a section conf
* In : 
    * file_name : name of the file conf
    * path : where is stored the conf file
    * section : the conf section name that you are looking for
* Out :
    * dict with all the conf param of the section
"""
def get_section_conf(file_name, path, section):

    logger.debug('Start to get conf')

    #San tests
    if not isinstance(file_name, str):
        logger.error('file_name param has to be a string')
        return False
    
    if not isinstance(section, str):
        logger.error('section param has to be a string')
        return False
        
    if not isinstance(path, str):
        logger.error('path param has to be a string')
        return False
    
    if not os.path.exists(path + '/' + file_name):
        logger.error('file {0} missing in {1}'.format(file_name, path))
        return False

    try:
        config = configparser.ConfigParser()
        config.read(path + '/'  +  file_name)
        config.sections()

        logger.debug('Conf loaded')
        
        if not section in config:
            logger.error('Missing section {0} in file {1}'.format(section, file_name))
            return False

        conf_r = config[section]

    except ValueError as e:
        logger.error('Unable to load conf file {}'.format(file_name))
        logger.error('{}'.format(e), exec_info = True)
        return False
    else:
        logger.info('Conf file {0}/{1} loaded'.format(file_name, section))
        return conf_r

"""
* Purpose : return a dict of a conf file
* In : 
    * file_name : name of the file conf
    * path : where is stored the conf file
    * section : the conf section name that you are looking for
* Out :
    * dict with all the conf
"""
def get_conf(file_name, path):

    logger.debug('Start to get conf')

    #San tests
    if not isinstance(file_name, str):
        logger.error('file_name param has to be a string')
        return False
    
    if not isinstance(path, str):
        logger.error('path param has to be a string')
        return False
    
    if not os.path.exists(path + '/' + file_name):
        logger.error('file {0} missing in {1}'.format(file_name, path))
        return False

    try:
        config = configparser.ConfigParser()
        config.read(path + '/'  +  file_name)
        config.sections()

        logger.debug('Conf loaded')
        
    except ValueError as e:
        logger.error('Unable to load conf file {}'.format(file_name))
        logger.error('{}'.format(e), exec_info = True)
        return False
    else:
        logger.info('Conf file {0}/{1} loaded'.format(file_name, section))
        return conf_r
