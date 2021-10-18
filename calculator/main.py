def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("You entered invalid numbers. Please try again.")
            continue
        break

   
    while True:
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("You entered invalid numbers. Please try again.")
            continue
        break

    while True:
        operator = input("Enter operator (+, -, * or /): ")
        if operator == "+":
            print(num1 + num2)
            break
        elif operator == "-":
            print(num1 - num2)
            break
        elif operator == "*":
            print(num1 * num2)
            break
        elif operator == "/":
            print(num1 / num2)
            break
        else:
            return False
 
calculator()