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
