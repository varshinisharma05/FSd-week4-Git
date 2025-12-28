# Simple Calculator Project

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

if __name__ == "__main__":
    print("Calculator started.")