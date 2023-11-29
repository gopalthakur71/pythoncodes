#Interact with API or CLI
#Get pull rquest information of a repo using python. we will use API call method. 
#Flow chart
''' --> import module "request"
    --> url for API request call . Get a pull request from git docs. 
    --> convert Json into dictionary because python can perform operation on dictionary. 
'''

import requests

response =  requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details = response.json()

for i in range(len(details)):
    print(details[i]['user']['login'])