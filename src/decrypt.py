from type.point import Point
from type.ECEG import ECEG
from image_processor import read_image, search_image
from utils.functions import makeBinToHex
from utils.calculation import makeStringToPairPointValue, getPointFromPairPointValue
import time 

def decryption():

  # Check Validity of Image
  image = None
  image = read_image()

# Make sure the image is valid
  if (image is not None):
    aVal = int(input("Insert 'a' Value: "))
    bVal = int(input("Insert 'b' Value: "))
    pVal = int(input("Insert 'p' Value: "))
    basePointXVal = int(input("Insert x Value of Base Point: "))
    basePointYVal = int(input("Insert y Value of Base Point: "))
    used_private_key = int(input("Insert Private Key to be used: "))
    encrypted_attrib = int(input("Insert Encrypted Attribute: "))

    # Initiate ECEG
    eceg = ECEG()
    eceg.setValue(aVal, bVal, pVal)
    basePoint = Point(basePointXVal, basePointYVal)
    eceg.setBasePoint(basePoint)

    begin = time.time()
    # Search for encrypted val
    encrypted_length = encrypted_attrib // (basePoint.y + 2 * basePoint.x)
    encrypted_value = search_image(image, basePoint, encrypted_length)
    hex_encrypted_value = makeBinToHex(encrypted_value).rjust(32, '0')
    print("")
    print(f"Encrypted Value Bin: {encrypted_value}")
    print(f"Encrypted Value Hex: {hex_encrypted_value}")

    pair_point_value = makeStringToPairPointValue(hex_encrypted_value)
    pair_point = getPointFromPairPointValue(pair_point_value)
    decrypted_value = eceg.decryptECEG(used_private_key, pair_point)

    # Display Decrypted
    print("")
    print(f"Decrypted Secret Point: {decrypted_value.getPointNumberValue()}")
    print(f"Decrypted Secret Point Hex: {decrypted_value.getPointValue()}")
    end = time.time()

    print(f"\nTotal runtime of the decryption process is {end - begin}") 


    
