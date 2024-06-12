import math

def makeNumToBin (num: int) -> str:
  return bin(num)[2:]

def makeNumToHex (num: int) -> str:
  return hex(num)[2:]

def makeHexToNum (hex: str) -> int:
  return int(hex, 16)

def makeBinToNum (bin: str) -> int:
  return int(bin, 2)

def makeHexToBin (hex: str) -> str:
  num = makeHexToNum(hex)
  return makeNumToBin(num)

def makeBinToHex (bin: str) -> str:
  num = makeBinToNum(bin)
  return makeNumToHex(num)

def isSquare(n: int) -> bool:
  return (math.sqrt(n) % 1 ) == 0

def positiveModulo (dividend: int, divisor: int) -> int:
  return ((dividend % divisor) + divisor) % divisor

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