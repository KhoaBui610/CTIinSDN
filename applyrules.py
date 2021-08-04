import re 

import subprocess 

import sys 

import json 

  

ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" 

  

def getJSON(MispJson): 

    with open(MispJson) as mj: 

        return json.load(mj) 

  

object = getJSON('./jsonmisp') 

get_object = object.get("Attribute") 

  

for threat in get_object: 

  i = threat["value"] 

  if(re.search(ip, i)): 

     ip1 = {"192.168.75.213/32", “192.168.75.214/32”} 

  

     for host in ip1: 

         flow = "{" + "\"nw_src\": \"" + host + "\", ""\"nw_dst\": \"" + i + "\", ""\"nw_proto\": \"ICMP\", \"actions\": \"DENY\", \"priority\": \"10\"} " 

         command = subprocess.run([ 

                   'curl', 

                   '-X', 

                   'POST', 

                   '-d', 

                   flow, 

                   'http://localhost:8080/firewall/rules/0000000000000001' 

         ], capture_output=True) 