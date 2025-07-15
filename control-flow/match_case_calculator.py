num1 = float(input("Enter the first number: "))
num2 = float(input(" Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
result = 0
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("No valid operation")


if result:
    print(f"The result is {result}.")