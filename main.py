print("Welcome to Calculi, a simple calculator in the terminal!")
print("\n")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

while True:
    try:
        operation = input("Enter operation (+, -, *, /, ^, or quit): ")
        if operation == "quit":
            print("\n")
            print("Thank you for using Calculi, Exiting")
            break
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if operation == "+":
            print(add(x, y))
        elif operation == "-":
            print(subtract(x, y))
        elif operation == "*":
            print(multiply(x, y))
        elif operation == "/":
            print(divide(x, y))
        elif operation == "^":
            print(power(x, y))
        else:
            print("Invalid operation")
    except ValueError:
        print("Erm, Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", str(e))

