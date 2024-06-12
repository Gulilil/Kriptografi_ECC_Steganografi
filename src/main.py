from type.ECEG import ECEG
from utils.number import generatePrimeNumber
from utils.functions import makeNumToHex, makeHexToNum, makeBinToHex
from utils.calculation import getKValue, makePairPointValueToString, makeStringToPairPointValue, getPointFromPairPointValue, getValueFromPairPoint
from encrypt import encryption
from decrypt import decryption

import numpy as np
import matplotlib.image as img
import os

if __name__ == "__main__":
  print("Choose (e) to Encrypt and (d) to Decrypt.")
  choice = input("-> ").upper()

  while (choice != "E" and choice != 'D'):
    print("Choose (e) to Encrypt and (d) to Decrypt.")
    choice = input("-> ").upper()

  if (choice == "E"):
    encryption()
  else: 
    decryption()
    






