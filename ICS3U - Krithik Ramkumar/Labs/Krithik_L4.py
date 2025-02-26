#-----------------------------------------------------------------------------
# Name:        Lists Lab
# Purpose:     Grocery List Sorter (Lists)
#
# Author:      Krithik Ramkumar
#
# Created:     24-02-2025
# Updated:     25-02-2025
# Copyright:   (c) Mr. Seidel 2018
# License:     The MIT License (MIT)
#-----------------------------------------------------------------------------

groceryList = []
print("-" * 50)
x = str(input("Enter Groceries:"))
print("-" * 50)


while True:
    if x not in groceryList and x != "!" and x != "remove":
        groceryList.append(x)
        print(groceryList)
        x = str(input("Enter Groceries:"))
        print("-" * 50)
    elif x == "remove":
        n = str(input("Enter removals:"))
        groceryList.remove(n)
    elif x == "!":
        print(groceryList[2])
        print(groceryList[-2])
        print(groceryList[2:6])
        print("-" * 50)
        print("Thanks for using my Grocery Sorter!")
        exit()



