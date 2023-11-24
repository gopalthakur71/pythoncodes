# Write a 

def calculate_total(jar):
    total = 0
    for money in jar:
        total += money
    return total

jar = [10, 20, 30, 40, 60, 70]  # Example list of numbers
result = calculate_total(jar)
print(result)  # This will print the total
