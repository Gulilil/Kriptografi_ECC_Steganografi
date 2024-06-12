from type.point import Point
from type.ECEG import ECEG

import matplotlib.image as img
import os

def decryption():
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

  aVal = input("Insert a Value: ")
  bVal = input("Insert b Value: ")
  pVal = input("Insert p Value: ")
  basePointXVal = input("Insert x Value of Base Point: ")
  basePointYVal = input("Insert y Value of Base Point: ")

  basePoint = Point(basePointXVal, basePointYVal)

  # Initiate ECEG
  eceg = ECEG()
  eceg.setValue(aVal, bVal, pVal)
  eceg.setBasePoint(basePoint)

  
