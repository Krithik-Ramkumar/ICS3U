#-----------------------------------------------------------------------------
# Name:        Looping Structures Lab
# Purpose:     Factorial Calculator (While Loop)
#
# Author:      Krithik Ramkumar
#
# Created:     24-02-2025
# Updated:     24-02-2025
# Copyright:   (c) Mr. Seidel 2018
# License:     The MIT License (MIT)
#-----------------------------------------------------------------------------

print("-" * 50)
n = int(input("Enter number: "))
print("-" * 50)
r = 1
num = 1

if n < 0:
    print("Invalid input")
else:
    while num <= n:
        r *= num
        num += 1
    print(r)



