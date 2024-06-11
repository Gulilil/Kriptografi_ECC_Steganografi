from type.point import Point
from utils.functions import modInverse, positiveModulo

def calculateGradient(p1: Point, p2: Point, pVal: int) -> int | None :
  modInv = modInverse(p2.x - p1.x, pVal)
  if (modInv):
    return positiveModulo((p2.y - p1.y) * positiveModulo(modInv, pVal), pVal)
  else:
    print("Null Mod Result. P1: (", p1.x, ", ", p1.y,") | P2: (", p2.x,", ", p2.y,")")
    return None
  
def calculateGradientHomogenous(p: Point, aVal: int, pVal: int) -> int | None:
  modInv = modInverse(2 * p.y, pVal)
  if (modInv):
    return positiveModulo( positiveModulo(3 * (p.x ** 2) + aVal, pVal) * positiveModulo (modInv, pVal), pVal)
  else:
    print("Null Mod Result. P: (", p.x, ", ", p.y,")")
    return None
  
def isPointInList (arr: list, p: Point):
  for point in arr:
    if (point.isSamePoint(p)):
      return True
  
  return False