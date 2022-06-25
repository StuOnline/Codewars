# Circles in Polygons
import math

def circle_diameter(sides, side_length): 
    print( side_length / math.tan(math.pi / sides))


circle_diameter(5, 10)
