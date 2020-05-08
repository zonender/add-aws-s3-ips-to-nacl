#!/usr/bin/env python3
import json
import requests

data = {}

# egress rules portion
data['egress'] = []
data['egress'].append({
  'rule_no': '200',
  'protocol': 'tcp',
  'allow_deny': 'allow',
  'cidr': '0.0.0.0/0',
  'icmp_type': 'null',
  'icmp_code': 'null',
  'port_from': '22',
  'port_to': '22'
})
data['egress'].append({
  'rule_no': '201',
  'protocol': 'tcp',
  'allow_deny': 'allow',
  'cidr': '0.0.0.0/0',
  'icmp_type': 'null',
  'icmp_code': 'null',
  'port_from': '22',
  'port_to': '22'
})

# ingress rules portion
data['ingress'] = []
data['ingress'].append({
  'rule_no': '200',
  'protocol': 'tcp',
  'allow_deny': 'allow',
  'cidr': '0.0.0.0/0',
  'icmp_type': 'null',
  'icmp_code': 'null',
  'port_from': '22',
  'port_to': '22'
})
data['ingress'].append({
  'rule_no': '201',
  'protocol': 'tcp',
  'allow_deny': 'allow',
  'cidr': '0.0.0.0/0',
  'icmp_type': 'null',
  'icmp_code': 'null',
  'port_from': '22',
  'port_to': '22'
})

#save
with open('nacl.json', 'w') as outfile: 
  json.dump(data, outfile)

# open file
with open('nacl.json', 'r') as json_file:
  data = json.load(json_file)
################################################################################################
################################################################################################
print("#########################################")
print("S3 IP RANGES IN US-EAST-1")
print("#########################################")

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']

selected_service = 'S3'
selected_region = 'us-east-1'

for item in ip_ranges:
  if item['service'] == selected_service and item['region'] == selected_region:
    print(item['ip_prefix'])





