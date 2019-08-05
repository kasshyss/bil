#!/usr/bin/env python
import lib.m_logger as log
import lib.m_conf as conf
import lib.m_request as request
import lib.m_file as f
import pandas as pd
import os

path = os.path.dirname(os.path.abspath(__file__))
cf = 'scrapping.ini'
section = 'QUERIES'

print(log.get_logger_level(''))
c = conf.get_section_conf(cf, path +'/conf', section)
print(c['guichet_lu'])
#d = request.request_html(str(c['guichet_lu']+'1'))
#print(d)
a = f.csv_to_df(path + '/save', 'test.csv')
print(a.shape[1])

s = f.df_to_csv(path + '/save', 'test_out.csv', a)
print(s)

s = f.append_df_to_csv(path + '/save', 'test_out.csv', a)
print(s)
print('fin')
