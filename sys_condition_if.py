import sys

type = sys.argv[1]

if type == "t2.micro":
    print('ok, It will charge you $2/day')

elif type == "t2.medium":
    print("This will charge $4/day")

elif type == "t2.xlarge":
    print("This will charge $6/day")
    
else:
    print("Please provide a valid instance type")
