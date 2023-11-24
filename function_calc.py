import sys


def sum(num1, num2):
    add = num1+num2
    return add

def subtraction(num1, num2):
    difference =  num1 - num2
    return difference

def product(num1, num2):
    product = num1*num2
    return product

def division(num1,num2):
    div = num1/num2
    return div

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "sum" or "add" or "+":
    output = sum(num1, num2)
    print(output)

if operation == "subtract" or "minus" or "-":
    output = subtraction(num1, num2)
    print(output)

if operation == "multiply" or "into" or "*" or "x":
    output = product(num1, num2)
    print(output)

if operation == "divide" or "by" or "/":
    output = division(num1, num2)
    print(output)