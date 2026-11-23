#trying out calculator from bros code

operator = input("Enter a mathematical operator: 'eg: + , - , * , /' ")
number1 = float(input("enter first number"))
number2 = float(input("enter second number"))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("please check your operator and enter a valid one")