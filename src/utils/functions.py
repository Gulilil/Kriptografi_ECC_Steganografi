import math
from ..type.point import Point

def makeNumToHex (num: int) -> str:
  return hex(num)

def makeHexToNum (hex: str) -> int:
  return int(hex)

def isSquare(n: int) -> bool:
  return (math.sqrt(n) % 1 ) == 0

def positiveModulo (dividend: int, divisor: int) -> int:
  return ((dividend % divisor) + divisor) % divisor

def isPointInList (arr: list, p: Point):
  for point in arr:
    if (point.isSamePoint(p)):
      return True
  
  return False

def gcd(a: int, b: int) -> int :
  while (b != 0):
    temp = b
    b = a % b
    a = temp
  
  return a

def modInverse(a: int, m: int) -> int:
  a = positiveModulo(a, m)
  if(gcd(a, m) != 1):
    print("The number is not invertible.")
    return None
  
  i = 0
  while (True):
    if ((i * a) % m == 1):
      return i
    
    i += 1

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