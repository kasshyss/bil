#-*- coding: utf-8 -*-
"""
* Purpose : run web requests
* Author : Meriadoc
* Log :
    * 05/08/2019 : Initial commit
"""


import urllib2
import m_logger as log

logger = log.get_logger('request', log.get_logger_level('warning'))


"""
* Purpose :
* In :
    * the requested url
* Out :
    * string
"""
def request_html(url):
    
    if not isinstance(url, str):
        logger.error('url : string require')
        return False

    try:
        logger.debug('Get new web page')
        result = urllib2.urlopen(url)
        contents = result.read()
        logger.debug(result.getcode())

    except urllib2.URLError as urle:
        logger.error('Fail to reach {}'.format(url))
        logger.error(''.format(urle.reason), exc_info = True)
        return False
    else:
        logger.info('Fetch web contents at {} without error'.format(url))
        return contents

