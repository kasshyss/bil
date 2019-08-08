"""
* Purpose : manage file interaction
* Author : Meriadoc
* Log :
    * 05/08/2019 : Initial commit
    * 08/08/2019 : Update append fct : remove index = false
    * 08/08/2019 : update with error_bad_lines in fct csv to df
"""

import m_logger as log
import pandas as pd
import os

logger = log.get_logger('file', log.get_logger_level('warning'))


"""
* Purpose : get a csv file stored on the disk and return a dataframe
* In :
    * file path
    * file name
* Out :
    * panda dataframe
"""
def csv_to_df(path, file_name):
    
    if not isinstance(path, str):
        logger.error('path : String require')
        return False

    if not isinstance(file_name, str):
        logger.error('file_name : String require')
        return False
    logger.debug( file_name.split('.').pop(-1)) 
    if file_name.split('.').pop(-1) != 'csv' :
        logger.error('Wrong file format, cvs require currently is {}'.format(file_name.split('.').pop(-1)))
        return False
    
    full_path = path + '/' + file_name
    
    if not os.path.exists(full_path):
        logger.error('File {0} missing in folder {1}'.format(file_name, path))
        return False
    
    logger.debug('Open file {}'.format(full_path))
    try:
        df = pd.read_csv(full_path , index_col = False, sep = ';', error_bad_lines = False)
    except ValueError as e:
        logger.error('Unable to read file {}'.format(full_path))
        logger.error(''.format(e), exc_info = True)
        return False
    else:
        logger.info('File {} loaded in dataframe'.format(file_name))
        return df

"""
* Purpose : save a panda dataframe into a csv
* In : 
    * Panda dataframe
    * target path
    * target file name
* Out :
    * None
"""
def df_to_csv(path, file_name, df):
     
    if not isinstance(path, str):
        logger.error('path : String require')
        return False

    if not isinstance(file_name, str):
        logger.error('file_name : String require')
        return False
    
    if file_name.split('.').pop(-1) != 'csv' :
        logger.error('Wrong file format, cvs require currently is {}'.format(file_name.split('.').pop(-1)))
        return False
    
    full_path = path + '/' + file_name
    
    if not isinstance(df, pd.DataFrame):
        logger.error('df : pandas DataFrame is requrie')
        return False
    
    logger.debug('Open file {}'.format(full_path))
    try:
        if os.path.exists(full_path):
            logger.info('Overide current file')
        df.to_csv(full_path , sep = ';', encoding='utf-8')
    except ValueError as e:
        logger.error('Unable to write file {}'.format(full_path))
        logger.error(e, exc_info = True)
        return False
    else:
        logger.info('File {} loaded in dataframe'.format(file_name))
        return True

"""
* Purpose : append a panda dataframe to an existe cvs
* In : 
    * target file
    * target path
    * panda dataframe
* Out :
    * None
"""
def append_df_to_csv(path, file_name, df):
     
    if not isinstance(path, str):
        logger.error('path : String require')
        return False

    if not isinstance(file_name, str):
        logger.error('file_name : String require')
        return False
    
    if file_name.split('.').pop(-1) != 'csv' :
        logger.error('Wrong file format, cvs require currently is {}'.format(file_name.split('.').pop(-1)))
        return False
    
    full_path = path + '/' + file_name
    
    if not isinstance(df, pd.DataFrame):
        logger.error('df : pandas DataFrame is requrie')
        return False
    
    logger.debug('Open file {}'.format(full_path))
    try:
        if os.path.exists(full_path):
            logger.info('Overide current file')
        df.to_csv(full_path , sep = ';', header = False, mode = 'a', encoding='utf-8')
    except ValueError as e:
        logger.error('Unable to read file {}'.format(full_path))
        logger.error(''.format(e), exec_info = True)
        return False
    else:
        logger.info('File {} loaded in dataframe'.format(file_name))
        return True
