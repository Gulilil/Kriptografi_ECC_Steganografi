import random
from constant import *

def getRandomNumber() -> int :
  return random.randint(THRESHOLD_RANGE)

def isPrime(n: int, k: int = 10) -> bool:
  if (n <= 1): return False
  if (n <= 3): return True
  if (n % 2 == 0): return False

  r = 0
  d = n - 1
  while (d % 2 == 0):
    r += 1
    d >>=1

def generatePrimeNumber() -> int:
  while (True):
    num = getRandomNumber()
    if (isPrime(num)):
      return num
    
def modExp(base: int, exp: int, mod: int) -> int:
  result = 1
  base = base % mod
  while(exp > 0):
    if (exp % 2 == 1):
      result = (result * base) % mod
    exp = exp >> 1
    base = (base * base) % mod