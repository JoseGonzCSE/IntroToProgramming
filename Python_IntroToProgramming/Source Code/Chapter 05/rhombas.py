# The rhombas module has functions that perform
# calculations related to rhombas.
import math 

# The area function accepts a rhombas diagonal lengths as an
# argument and returns the area of the Rhombas.
def Area ( diagonal_length_1,diagonoal_length_2):
    return((diagonal_length_1*diagonoal_length_2)/2)

# The perimeter function accepts a Rhombas side length
#  as arguments and returns the Rhombus
# perimeter.

def perimeter(area):
    return(4*area)