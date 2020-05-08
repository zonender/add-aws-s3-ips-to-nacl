#!/usr/bin/env python3
import json
import requests

################################################################################################
################################################################################################
print("#########################################")
print("S3 IP RANGES IN US-EAST-1")
print("#########################################")

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']

selected_service = 'S3'
selected_region = 'us-east-1'
s3_ip_list = []

for item in ip_ranges:
  if item['service'] == selected_service and item['region'] == selected_region:
    print(item['ip_prefix'])
    s3_ip_list.append(item['ip_prefix'])

################################################################################################
################################################################################################

data = {}

data['egress'] = []
data['ingress'] = []
port_from = 1234
port_to = 1234

# ingress
rule_number = 199
for ip in s3_ip_list:
  rule_number += 1
  data['ingress'].append({
    'rule_no': f'{rule_number}',
    'protocol': 'tcp',
    'allow_deny': 'allow',
    'cidr': f'{ip}',
    'icmp_type': 'null',
    'icmp_code': 'null',
    'port_from': f'{port_from}',
    'port_to': f'{port_to}'
  })

# egress
rule_number = 199
for ip in s3_ip_list:
  rule_number += 1
  data['egress'].append({
    'rule_no': f'{rule_number}',
    'protocol': 'tcp',
    'allow_deny': 'allow',
    'cidr': f'{ip}',
    'icmp_type': 'null',
    'icmp_code': 'null',
    'port_from': f'{port_from}',
    'port_to': f'{port_to}'
  })

# save
with open('nacl.json', 'w') as outfile: 
  json.dump(data, outfile)







