#!/usr/bin/env python 

import logging

import novaclient
from novaclient.v1_1 import client 

# enable debug logging of http request/response
logger = logging.getLogger('novaclient.client')
logger.setLevel(logging.DEBUG)
debug_stream = logging.StreamHandler()
logger.addHandler(debug_stream)

auth_url = 'http://10.100.20.22:5000/v2.0'
user = 'admin'
password = 'devstack'
project = 'demo'
region = 'RegionOne'
service = 'compute'

nova = client.Client(user, password, project, auth_url,
                     region_name=region, service_type=service)

results = nova.images.list(detailed=True)
for image in results:
    print image.id, image.name, image.status

