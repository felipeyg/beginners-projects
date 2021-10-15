

def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, * or /): ")
    num2 = float(input("Enter second number: "))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("You entered a invalid number or operator. Please try again.")
        return calculator()

calculator()