import random
from utils.constant import LOWER_THRESHOLD, UPPER_THRESHOLD

def getRandomNumber() -> int :
  return random.randint(LOWER_THRESHOLD, UPPER_THRESHOLD)

def isPrime(n: int, k: int = 10) -> bool:
  if (n <= 1): return False
  if (n <= 3): return True
  if (n % 2 == 0 or n % 3 == 0): return False

  i = 5
  while i * i <= n:
      if n % i == 0 or n % (i + 2) == 0:
          return False
      i += 6
  return True

def generatePrimeNumber() -> int:
  while (True):
    num = getRandomNumber()
    if (isPrime(num)):
      return int(num)
    
def modExp(base: int, exp: int, mod: int) -> int:
  result = 1
  base = base % mod
  while(exp > 0):
    if (exp % 2 == 1):
      result = (result * base) % mod
    exp = exp >> 1
    base = (base * base) % mod