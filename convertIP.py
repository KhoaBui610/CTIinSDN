import re 

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

     print(i) 