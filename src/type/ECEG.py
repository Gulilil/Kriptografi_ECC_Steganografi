from type.point import Point
from type.ECC_base import ECCBase
from type.incrementing_point import IncrementingPoint
from type.pair_point import PairPoint, PairPointValue
from utils.number import generatePrimeNumber
from utils.functions import positiveModulo, makeHexToNum, makeNumToHex
from utils.constant import INFINITY_POINT
from utils.calculation import calculateGradient, calculateGradientHomogenous
import math
import random

class ECEG :

  def __init__(self):
    self.aVal = generatePrimeNumber()
    self.bVal = generatePrimeNumber()
    self.pVal = generatePrimeNumber()
    self.points = []
    self.basePoint = Point(0, 0)
    self.calculatePoints()

  def calculatePoints (self):
    self.points = []
    check = 4 * (self.aVal ** 3) + 27 * (self.bVal ** 2) 
    while (check == 0):
      self.aVal = generatePrimeNumber()
      self.bVal = generatePrimeNumber()
      check = 4 * (self.aVal ** 3) + 27 * (self.bVal ** 2) 

    for i in range (self.pVal-1):
      res = self.calculateY(i)
      selection1 = (res % 1 == 0)
      selection2 = (res > 0 and res < self.pVal)
      if (selection1 and selection2):
        self.points.append(Point(i, res))
        self.points.append(Point(i, self.pVal-res))
    
  def setValue (self, a: int, b: int, p: int):
    self.aVal = a
    self.bVal = b
    self.pVal = p
    self.calculatePoints()

  def getValue (self) -> ECCBase:
    data = ECCBase(self.aVal, self.bVal, self.pVal, self.basePoint)
    return data
  
  def setBasePoint (self, p: Point):
    self.basePoint = p

  def calculateY (self, x: int) -> int:
    return math.sqrt( ((x ** 3) + self.aVal * x + self.bVal) % self.pVal)
  
  def calculateCoorX (self, p1: Point, p2: Point, m: int) -> int:
    res = positiveModulo( (positiveModulo(m ** 2, self.pVal) - positiveModulo(p1.x, self.pVal) - positiveModulo(p2.x, self.pVal)), self.pVal)
    return res
  
  def calculateCoorY (self, p1: Point, p2: Point, m: int) -> int:
    xR = self.calculateCoorX(p1, p2, m)
    res = positiveModulo(( positiveModulo(m, self.pVal) * positiveModulo(p1.x - xR, self.pVal) - positiveModulo(p1.y, self.pVal)), self.pVal)
    return res
  
  def addPoint (self, p1: Point, p2: Point) -> Point:

    if (p1.isInverse(p2, self.pVal)):
      return INFINITY_POINT
    
    if (p1.isSamePoint(INFINITY_POINT)):
      return p2
    elif (p2.isSamePoint(INFINITY_POINT)):
      return p1
    
    if (p1.isSamePoint(p2) and p1.y == 0):
      return INFINITY_POINT
    
    m = 0
    if (p1.isSamePoint(p2)):
      m = calculateGradientHomogenous(p1, self.aVal, self.pVal)
    else:
      m = calculateGradient(p1, p2, self.pVal)
    
    x = int(self.calculateCoorX(p1, p2, m))
    y = int(self.calculateCoorY(p1, p2, m))

    return Point(x, y)
  
  def minusPoint (self, p1: Point, p2: Point) -> Point:
    newP2 = Point(0, 0)
    newP2.copyPoint(p2)
    newP2.changeToInverse()
    return self.addPoint(p1, newP2)

  
  def multiplyPoint(self, p: Point, n: int | str) -> Point:

    if isinstance(n, str):  
      n = makeHexToNum(n)

    multiplicationDict = list()
    exp = 1
    idx = 0
    tempPoint = Point(0, 0)
    tempPoint.copyPoint(p)

    # Making Dictionary
    while (exp <= n):
      currentIncrementpoint = IncrementingPoint(exp, tempPoint)
      multiplicationDict.append(currentIncrementpoint)
      exp *= 2
      idx += 1

      newTempPoint = self.addPoint(tempPoint, tempPoint)
      tempPoint = newTempPoint

    idx = len(multiplicationDict) -1
    decrementalN = n
    resPoint = INFINITY_POINT

    # Multiplication 
    while (decrementalN > 0):
      while (multiplicationDict[idx].exponent > decrementalN):
        idx -= 1

      tempIncrementPoint = multiplicationDict[idx]
      resPoint = self.addPoint(resPoint, tempIncrementPoint.point)
      decrementalN -= tempIncrementPoint.exponent

    return resPoint
    

  def getRandomPoint(self) -> Point:
    self.basePoint = self.points[ math.floor( random.randint( 0, len(self.points) - 1))]
    temp = Point(self.basePoint.x, self.basePoint.y)
    return temp
  
  def searchPoint(self, p: Point) -> Point | None :
    for point in self.points:
      if (p.isSamePoint(point)):
        return point
      
    return None

  def encryptECEG (self, k: int, basePoint: Point, secretPoint: Point, publicKey: Point) -> PairPoint:
    kPb = self.multiplyPoint(publicKey, k)
    resPairPoint = PairPoint(self.multiplyPoint(basePoint, k), self.addPoint(secretPoint, kPb))
    return resPairPoint
  
  def decryptECEG (self, privateKey: int | str, pairPoint: PairPoint) -> Point :
    p1 = pairPoint.p1
    p2 = pairPoint.p2
    bkB = self.multiplyPoint(p1, privateKey)
    return self.minusPoint(p2, bkB)
  
  def getValueFromPairPoint(self, pairPoint: PairPoint) -> PairPoint:
    pairPointVal = PairPointValue(pairPoint.p1.getPointValue(), pairPoint.p2.getPointValue())
    return pairPointVal
  
  def getPointFromPairPointValue(self, pairPointVal : PairPointValue) -> PairPoint:
    p1 = Point(0,0)
    p1.setPointValue(pairPointVal.p1Val)
    p2 = Point(0,0)
    p2.setPointValue(pairPointVal.p2Val)

    pairPoint = PairPoint (p1, p2)
    return pairPoint
  
  def makePairPointValueToString (self, pairPointVal: PairPointValue) -> str:
    return pairPointVal.p1Val + pairPointVal.p2Val
  
  def makeStringToPairPointValue(self, val: str) -> PairPointValue:
    p1Val = val[:16]
    p2Val = val[16:]
    pairPointVal = PairPointValue(p1Val, p2Val)
    return pairPointVal
  
  def getKValue (self) -> int:
    k = generatePrimeNumber()
    while (k < 1 or k > self.pVal -1):
      k = generatePrimeNumber()
    return k
  