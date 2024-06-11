# To be imported by other file 

from ..type.point import Point
import math

UPPER_THRESHOLD = 5000000
LOWER_THRESHOLD = 2500000
THRESHOLD_RANGE = (LOWER_THRESHOLD, UPPER_THRESHOLD)

INFINITY_POINT = Point(math.inf, math.inf)