# This program calculates Area and Perimeters of multiple shapes using muiltiple Modules
# Inputs: Radius,Lengths,Diagonal Lengths, and Lengths
# Outputs: Circumference, Area, or Perimeter
# Written by: Our Textbook
# Modified by:  Jose Gonzalez
# Modified Date: March 1,2020


# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle, rectangle, Stadium, and rhombas modules.
import circle
import rectangle
import Stadium
import rhombas

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
AREA_STADIUM_CHOICE =5
PERIMETER_STADIUM_CHOICE=6
AREA_RHOMBAS_CHOICE=7
PERIMETER_RHOMBAS_CHOICE=8
QUIT_CHOICE = 9

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is', \
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', \
                  rectangle.perimeter(width, length))
        elif choice == AREA_STADIUM_CHOICE:
            radius= float(input("Enter the stadium radius:"))
            width= float(input("Enter the stadiums width"))
            print('The Area is',\
                    Stadium.area(radius, width))
        elif choice == PERIMETER_STADIUM_CHOICE:
            radius= float(input("Enter the stadium radius:"))
            width= float(input("Enter the stadiums width"))
            print('The Perimeter is',\
                    Stadium.Perimeter(radius,width))
        elif choice == AREA_RHOMBAS_CHOICE:
             diagonal_length_1= float(input("Enter the rhombas first diagonal length:"))
             diagonoal_length_2= float(input("Enter the rhombas second diagonal length:"))
             print('The Area is',\
                    rhombas.Area(diagonal_length_1, diagonoal_length_2))
        elif choice == PERIMETER_RHOMBAS_CHOICE:
             area= float(input("Enter the Rhombus area:"))
             print('The Perimeter is',\
                    rhombas.perimeter(area))
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
    
# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Area of a stadium')
    print('6) Perimeter of a stadium')
    print('7) Area of a rhombus')
    print('8) Perimeter of a rhombus')
    print('9) Quit')

# Call the main function.
main()
