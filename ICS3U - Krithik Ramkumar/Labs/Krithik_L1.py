#-----------------------------------------------------------------------------
# Name:        Basics Lab Project
# Purpose:     Program which gathers input from user and does an operation with
#              it. Here I am trying to include all the operations available in
#              python
#
# Author:      Krithik Ramkumar
#
# Created:     20-Feb-2025
# Updated:     22-Feb-2025
# Copyright:   (c) Mr. Seidel 2018
# License:     The MIT License (MIT)
#-----------------------------------------------------------------------------

print("-" * 50)

x = int(input("Enter your first number: "))
oper = str(input("Enter your operation: "))
y = int(input("Enter your second number: "))

print("-" * 50)

if oper == "+":
    print("-" * 50)
    print(x + y)
    print("-" * 50)
elif oper == "-":
    print("-" * 50)
    print(x - y)
    print("-" * 50)
elif oper == "*":
    print("-" * 50)
    print(x * y)
    print("-" * 50)
elif oper == "/":
    print("-" * 50)
    print(x / y)
    print("-" * 50)
elif oper == "**":
    print("-" * 50)
    print(x ** y)
    print("-" * 50)
elif oper == "%":
    print("-" * 50)
    print(x % y)
    print("-" * 50)
else:
    print("-" * 50)
    print("Invalid operation")
    print("-" * 50)



