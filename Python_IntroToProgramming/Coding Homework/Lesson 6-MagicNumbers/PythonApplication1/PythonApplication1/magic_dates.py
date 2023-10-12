# This program Determines if a number is "magic"
# Inputs:  Month, Day, Two digit year
# Outputs: True or False?
# Written by: Jose Gonzalez
# Modified Date: Feb,10,2002

#Start
print("Please use me to determine if a number is magical please\n ")

#User input

Month = int(input("Please enter the month number:"))

Day = int(input("Please enter the day number:"))

year= int(input("Please enter a two-digit year:"))

# Calculations/ Output

if Month == 0 or Month>12:
        print("\nI Have never heard of that month before??\n")

if Day== 0 or Day>31:
        print("\nI really wish we had",Day,'days. Wouldnt that be cool?\n')

if year>99:
        print("\n very cool year! but uh... you cant use that.\n")


 #Required Output
if Month * Day == year:
    print("\nThat is Indeed a Magical Date!")
else:
    print("\nIn the end, it wasn't very magical.")