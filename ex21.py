def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")
age = add(18, 5)
height = subtract(175, 5)
weight = multiply(28, 2)
iq = divide(375, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
