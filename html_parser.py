#-*- coding: utf-8 -*-

"""
* Purpose : parse html web page thank to beautifull soup
* Author : Meriadoc
* Log :
    * 05/08/2019 : PB : Initial Commit
* TODO : Make generic reserach
"""

import lib.m_logger as log
from bs4 import BeautifulSoup

logger = log.get_logger('html_parser',log.get_logger_level('debug'))

"""
Purpose : parse code nace web page from guicher lu
In :
    * html page
* Out :
    * dict
"""
def code_nace(html):
    
    results = {}

    logger.debug('Start parse web page ')
    desc = BeautifulSoup(html,'html.parser')
    
    results['compagny_name'] = desc.find("body").find("h2").getText()
    results['address'] = desc.find("body").find("p").getText().replace('L-',',L-')
    results['code_nace'] = desc.find("body").find(attrs={"class":"nacecode"}).getText()
    results['code_nace_desc'] = desc.find("body").find(attrs={"class":"nacecode-category"}).getText()
    return results
