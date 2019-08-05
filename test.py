#!/usr/bin/env python
import lib.m_logger as log
import lib.m_conf as conf
import lib.m_request as request
import os

path = os.path.dirname(os.path.abspath(__file__))
cf = 'scrapping.ini'
section = 'QUERIES'

print(log.get_logger_level(''))
c = conf.get_section_conf(cf, path +'/conf', section)
print(c['guichet_lu'])
d = request.request_html(str(c['guichet_lu']+'1'))
print(d)
