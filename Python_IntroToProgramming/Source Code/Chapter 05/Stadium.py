# The Stadium module has functions that perform
# calculations related to Stadiums.

import math
# The area function accepts a Stadiums radius as an
# argument and returns the area of the Stadium.

def area(radius,width):
    return (math.pi* (radius**2)) + 2* radius * width

# The perimeter function accepts a Stadiums width/ area
#  as arguments and returns the Stadiums
# perimeter.

def Perimeter(radius,width):
    return 2 * ((math.pi*radius)+width)

