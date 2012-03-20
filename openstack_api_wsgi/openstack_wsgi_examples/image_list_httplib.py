#!/usr/bin/env python 

import urllib2
import json

def get_keystone_token():
    """authenticate against keystone identity service
    returns an auth token, and the service url

    """
    user = 'admin'
    password = 'devstack'
    project = 'demo'
    auth_url = 'http://10.100.20.22:5000/v2.0/tokens'

    auth_request = urllib2.Request(auth_url)
    auth_request.add_header('Content-Type', 'application/json;charset=utf8')
    auth_request.add_header('Accept', 'application/json')
    auth_request.add_header('User-Agent', 'python-mikeyp')

    auth_data = {"auth": 
        {"tenantName": project, 
         "passwordCredentials": {
            "username": user, 
            "password": password}
        }
    }
    auth_request.add_data(json.dumps(auth_data))
    auth_response = urllib2.urlopen(auth_request)
    response_data = json.loads(auth_response.read())

    token = response_data['access']['token']['id']

    service_list = response_data['access']['serviceCatalog']
    for s in service_list:
        if s['type'] == 'compute' and s['name'] == 'Compute Service':
            break
    nova_url = s['endpoints'][0]['publicURL']
    return (token, nova_url)

token, service_url  = get_keystone_token()

image_api = service_url + '/images/detail'

images_request = urllib2.Request(image_api)
images_request.add_header('Content-Type', 'application/json;charset=utf8')
images_request.add_header('Accept', 'application/json')
images_request.add_header('User-Agent', 'python-mikeyp')
images_request.add_header('X-Auth-Token', token)
images_request.add_header('X-Auth-Project-Id', 'demo')

image_response = urllib2.urlopen(images_request)
image_data = json.loads(image_response.read())
print json.dumps(image_data, indent=4)
