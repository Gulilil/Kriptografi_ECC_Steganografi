from type.ECEG import ECEG
from utils.number import generatePrimeNumber
from utils.functions import makeBinToHex, makeHexToBin
from utils.calculation import getKValue, makePairPointValueToString, getValueFromPairPoint

import numpy as np
import matplotlib.image as img
import os

def encryption():
  cwd = os.getcwd()
  test_dir = os.path.join(cwd, "test")

  # Check Validity of Image
  is_valid = False
  image = None
  while (not is_valid):
    try :
      print("Make sure to insert the image inside the /test folder.")
      filename = input("Insert the image filename: ")
      file_path = os.path.join(test_dir, filename)
      image = img.imread(file_path)
      is_valid = True
    except:
      print("Image not found! Please make sure to enter a valid image filename.")

  # Make sure the image is valid
  if (image is not None):
    height = image.shape[0]
    width = image.shape[1]
    print(f"Image {filename} has the height of {height}px and width of {width}px.")

    # Initiate the ECC (ECEG)
    eceg = ECEG()
    print(f"ECC Data:\n a: {eceg.aVal}\n b: {eceg.bVal}\n p: {eceg.pVal}")
    base_point = eceg.getRandomPoint()
    print(f"Base Point: {base_point.getPointNumberValue()}")

    # User Data
    a_private_key = generatePrimeNumber()
    b_private_key = generatePrimeNumber()
    a_public_key = eceg.multiplyPoint(base_point, a_private_key)
    b_public_key = eceg.multiplyPoint(base_point, b_private_key)

    print(f"\nUser A Data:\n Private Key: {a_private_key}\n Public Key: {a_public_key.getPointNumberValue()}")
    print(f"\nUser B Data:\n Private Key: {b_private_key}\n Public Key: {b_public_key.getPointNumberValue()}")

    # Secret Point
    secret_point = eceg.getRandomPoint()
    k = getKValue(eceg.pVal)
    print(f"\nSecret Point: {secret_point.getPointNumberValue()}")
    print(f"K Value: {k}")

    # Encrypt Secret Point
    pair_point = eceg.encryptECEG(k, base_point, secret_point, b_public_key)
    pair_point_value = getValueFromPairPoint(pair_point)
    encrypted_value = makePairPointValueToString(pair_point_value)
    binary_encrypted_value = makeHexToBin(int(encrypted_value, 16))
    print("")
    print(f"Encrypted Value Hex: {encrypted_value}")
    print(f"Encrypted Value Bin: {binary_encrypted_value}")

    # Decrypt Secret Point
    print("")
    bin_to_hex = makeBinToHex(binary_encrypted_value).rjust(32, '0')
    print(f"Bin to Hex {bin_to_hex}")