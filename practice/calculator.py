def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    if operation == "+":
        result = add(num1, num2)
        print(f"The result is {result}.")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"The result is {result}.")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"The result is {result}.")
    elif operation == "/":
        result = divide(num1, num2)
        print(f"The result is {result}.")
    else:
        print("Invalid operation selected.")