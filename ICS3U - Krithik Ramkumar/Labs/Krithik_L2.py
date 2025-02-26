#-----------------------------------------------------------------------------
# Name:        Conditionals Lab
# Purpose:     Course Grade Checker (Conditional Statements)
#
# Author:      Krithik Ramkumar
#
# Created:     24-02-2025
# Updated:     24-02-2025
# Copyright:   (c) Mr. Seidel 2018
# License:     The MIT License (MIT)
#-----------------------------------------------------------------------------

print("-" * 50)
grade = int(input("Enter grade: "))
print("-" * 50)

if grade > 100 or grade < 0:
    print("Invalid Grade")
elif grade >= 80:
    print("Your grade is exceeding expectations")
elif grade >= 70:
    print("Your grade is meeting expectations")
elif grade >= 50:
    print("Your grade needs improvement")
else:
    print("Your grade is a failing grade")



