#!/usr/bin/env python 

# -*- coding: utf-8 -*- 

  

misp_url = 'https://192.168.75.185' 

misp_key = 'DO6oV337NJCFakfNiqwjgOzJz1ioER5vKzVE8C5N'  

misp_verifycert = False 

relative_path = '' 

body = None 

  

from pymisp import ExpandedPyMISP 

  

misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert) 

misp.direct_call(relative_path, body) 

misp_client_cert = '' 

proofpoint_sp = '<proofpoint service principal>'  

proofpoint_secret = '<proofpoint secret>' 