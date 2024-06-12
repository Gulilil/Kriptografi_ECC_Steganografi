from type.point import Point
from type.ECEG import ECEG
from image_processor import read_image

import os

def decryption():

  # Check Validity of Image
  image = None
  image = read_image()

# Make sure the image is valid
  if (image is not None):
    aVal = input("Insert a Value: ")
    bVal = input("Insert b Value: ")
    pVal = input("Insert p Value: ")
    basePointXVal = input("Insert x Value of Base Point: ")
    basePointYVal = input("Insert y Value of Base Point: ")
    encrypted_length = input("Insert encrypted length: ")
    used_private_key = input("Insert Private Key to be used: ")

    # Initiate ECEG
    eceg = ECEG()
    eceg.setValue(aVal, bVal, pVal)
    basePoint = Point(basePointXVal, basePointYVal)
    eceg.setBasePoint(basePoint)

  
