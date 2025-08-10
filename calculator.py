# Simple Calculator 
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
operation = input("enter an operation (+ or -): ")

if operation == "+":
result = num1 + num2 
elif operation == "-":
 result = num1 - num2 
else:
result = "invalid operation"

print("result:", result)
