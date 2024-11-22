import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error:Invalid Input.")
    sys.exit(1)

def divide(x, y):
    return x / y

try:
    result = divide(x, y)
except ZeroDivisionError:
    print("Error: Cannot divite by 0.")
    sys.exit(1)

print(f"result = {result}")
