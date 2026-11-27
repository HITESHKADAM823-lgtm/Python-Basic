a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Addition =", a + b)
    case "-":
        print("Subtraction =", a - b)
    case "*":
        print("Multiplication =", a * b)
    case "/":
        print("Division =", a / b)
    case _:
        print("Invalid operator")