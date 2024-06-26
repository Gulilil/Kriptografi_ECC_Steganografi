from utils.functions import makeHexToNum, makeNumToHex

class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def setValue(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def copyPoint(self, p: object):
    self.x = p.x
    self.y = p.y

  def isSamePoint(self, p: object) -> bool:
    return self.x == p.x and self.y == p.y
  
  def isInverse (self, p: object, pVal: int) -> bool:
    return self.x == p.x and self.y == abs(pVal - p.y)
  
  def getPointNumberValue(self) -> str:
    return "x: "+str(self.x)+", y: "+str(self.y)
  
  def getPointValue (self) -> str:
    xHex = makeNumToHex(int(self.x)).rjust(8, '0')
    yHex = makeNumToHex(int(self.y)).rjust(8, '0')
    return xHex + yHex
  
  def setPointValue (self, val: str):
    xHex = val[:8]
    yHex = val[8:]
    self.x = makeHexToNum(xHex)
    self.y = makeHexToNum(yHex)

  def changeToInverse (self):
    self.y *= -1