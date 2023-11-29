import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

try: 
    div = num1/num2
except ZeroDivisionError:
    print("We can not divide any number by 0. Plase provide any other number")