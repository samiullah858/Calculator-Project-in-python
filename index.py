while True:
    num1 = input("Enter the Number 1 = ")
    try:
        num1 = float(num1)
        break
    except:
        print("invalid Number")
while True:
    num2 = input("enter the Number 2 = ")
    try:
        num2 = float(num2)
        break
    except:
        print("Invalid Number")
sign = input("Enter the Sign = ")
result = 0
if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 + num2
elif sign == '*':
    result = num1 + num2
elif sign == '%':
    result = num1 + num2
elif sign == '/':
    if num2 != 0:
        result = num1 + num2
    else:
        print("The Number 2 is invalid")
else:
    print("Try Again")
print("Result = ", result)
