from type.point import Point
from utils.functions import modInverse, positiveModulo
from utils.number import generatePrimeNumber
from type.pair_point import PairPoint, PairPointValue

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

def getValueFromPairPoint(pairPoint: PairPoint) -> PairPoint:
    pairPointVal = PairPointValue(pairPoint.p1.getPointValue(), pairPoint.p2.getPointValue())
    return pairPointVal
  
def getPointFromPairPointValue(pairPointVal : PairPointValue) -> PairPoint:
  p1 = Point(0,0)
  p1.setPointValue(pairPointVal.p1Val)
  p2 = Point(0,0)
  p2.setPointValue(pairPointVal.p2Val)

  pairPoint = PairPoint (p1, p2)
  return pairPoint

def makePairPointValueToString (pairPointVal: PairPointValue) -> str:
  return pairPointVal.p1Val + pairPointVal.p2Val

def makeStringToPairPointValue(val: str) -> PairPointValue:
  p1Val = val[:16]
  p2Val = val[16:]
  pairPointVal = PairPointValue(p1Val, p2Val)
  return pairPointVal

def getKValue (pVal) -> int:
  k = generatePrimeNumber()
  while (k < 1 or k > pVal -1):
    k = generatePrimeNumber()
  return k
  