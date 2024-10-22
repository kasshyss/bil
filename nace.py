#!/usr/bin/env python
#-*- coding utf-8 -*-

"""
* Purpose : parse gichet lu nace web page
* Author : Meriadoc
* Log :
    * 05/08/2019 : Initial Commit
    * 07/08/2019 : Push value into conf file
    * 08/08/2019 : Append data insead of override in result file
    * 08/08/2019 : Add keyboard interrupt management
"""

import lib.m_logger as log
import lib.m_conf as conf
import lib.m_file as f
import lib.m_request as request
import html_parser as parse
import os
import sys
import time as t
import pandas as pd
from datetime import datetime

logger = log.get_logger('nace_main', log.get_logger_level('info'))

logger.info('Init script')

local_path = os.path.dirname(os.path.abspath(__file__))
local_path = str(local_path)
web_target = str(conf.get_section_conf('scrapping.ini', local_path + '/conf', 'WEB_TARGET')['guichet_lu'])
output_conf = conf.get_section_conf('scrapping.ini', local_path + '/conf', 'OUTPUT')
sleep_time = float(conf.get_section_conf('scrapping.ini', local_path + '/conf', 'SCRIPT')['sleep'])
result = str(output_conf['result'])  
file_name =  str(output_conf['file_name'])
backup = str(output_conf['backup'])
nace_col = conf.get_section_conf('scrapping.ini', local_path + '/conf', 'NACE')['col'].split(',')
# TODO Exit codes

id = 1

logger.info('Check if {} already exist'.format(output_conf['file_name']))
if os.path.exists(local_path +'/'+ result  + '/' + file_name):
    # get df
    nace_df = f.csv_to_df(local_path + '/'  + result, file_name)
    nace_df = nace_df.drop_duplicates(keep = 'first')
    # back up df
    bckp_name = 'backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S'))+ '_'  + file_name
    s = f.df_to_csv(local_path + '/'  + backup , bckp_name, nace_df)
    logger.info('Backup current file as {}'.format(bckp_name))
    if s == False:
        logger.error('Fail to save backup file')
        logger.error('Initialisation fail')
        sys.exit(-1)
    #set up flags
    if nace_df.empty:
        id = 1
    else:
        id = int(nace_df['id'].max()) + 1
    nace_df = pd.DataFrame(columns = nace_col)
    logger.info('Start at id {}'.format(id))

else:

    logger.info('New run from strach')
    nace_df = pd.DataFrame(columns = nace_col)
    s = f.df_to_csv(local_path + '/'  +  result, file_name, nace_df)
    if s == False:
        logger.error('Initialisation fail')
        sys.exit(-1)

logger.info('Start parsing')
run = True
while run:
    try:
        nace_data = {} 
        if id % 10 == 0:
            logger.info('Status current run : {} ids checked'.format(id))
            s = f.append_df_to_csv(local_path + '/'  + result, file_name, nace_df)
            nace_df = pd.DataFrame(columns = nace_col)

            if s == False:
                logger.error('Run fail at id {}'.format(id))
                sys.exit(-1)
        html = request.request_html(web_target + str(id))
        if html == False:
            run = False
        nace_data = parse.code_nace(html)
        nace_df = nace_df.append({ 
            'id' : id, 
            'compagny_name' : nace_data['compagny_name'],
            'address' : nace_data['address'],
            'code_nace': nace_data['code_nace'],
            'code_nace_desc' : nace_data['code_nace_desc']
            }, ignore_index = True)
        id = id + 1
        t.sleep(sleep_time)
    except KeyboardInterrupt:
        logger.warning('Script ended by user')
        s = f.append_df_to_csv(local_path + '/'  + result, file_name, nace_df)

        if s == False:
            logger.error('Fail to save dataframe at script closing')
            sys.exit(-1)
        logger.info('Script end')
        sys.exit(0)

logger.info('all ids checked')
s = f.append_df_to_csv(local_path + '/'  + result, file_name, nace_df)
if s == False:
    logger.error('Run fail at id {}'.format(id-1))
    sys.exit(-1)

logger.info('script end')
sys.exit(1)
