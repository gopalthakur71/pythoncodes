def calculate_tax1():
    price = int(input("Please enter the bill :- "))
    final_bill = price + price*0.1
    print(f'The final price after 10% of tax is {final_bill}')


calculate_tax1()

def calculate_tax(price):
    price += price*0.2
    return price

final_bill = int(input("Please enter the final bill"))
result = calculate_tax(final_bill)
print(f"The final bill after 20% tax is {result}")

