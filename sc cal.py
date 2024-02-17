import math
import numpy as np


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Square root of a negative number"
    return np.sqrt(x)

def sin(x):
    return np.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

def log(x):
    if x <= 0:
        return "Error: Logarithm of a non-positive number"
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "Error: Natural logarithm of a non-positive number"
    return math.log(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial of a negative number"
    if x == 0:
        return 1
    return x * factorial(x - 1)

print("Welcome to the Python Scientific Calculator!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Sin")
print("8. Cos")
print("9. Tan")
print("10. Arcsin")
print("11. Arccos")
print("12. Arctan")
print("13. Logarithm")
print("14. Natural Logarithm")
print("15. Factorial")

choice = int(input("Enter the number of the operation you want to perform: "))

if choice in [1, 2, 3, 4, 5]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
elif choice in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    num = float(input("Enter the number: "))
else:
    print("Invalid choice")
    exit()

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
elif choice == 5:
    print("Result:", power(num1, num2))
elif choice == 6:
    print("Result:", sqrt(num))
elif choice == 7:
    print("Result:", sin(num))
elif choice == 8:
    print("Result:", cos(num))
elif choice == 9:
    print("Result:", tan(num))
elif choice == 10:
    print("Result:", arcsin(num))
elif choice == 11:
    print("Result:", arccos(num))
elif choice == 12:
    print("Result:", arctan(num))
elif choice == 13:
    print("Result:", log(num))
elif choice == 14:
    print("Result:", ln(num))
elif choice == 15:
    print("Result:", factorial(num))
