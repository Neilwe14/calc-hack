a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
operator = input("Please enter an operator (+ - / *): ")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b


if operator == "+":
    print(addition(a, b))
elif operator == "-":
    print(subtraction(a, b))
elif operator == "*":
    print(multiplication(a, b))
elif operator == "/":
    print(division(a, b))
else:
    print(f"{operator},please enter a valid operator!")
