from type.ECEG import ECEG
from type.point import Point
from utils.number import generatePrimeNumber
from utils.functions import makeBinToHex, makeHexToBin
from utils.calculation import getKValue, makePairPointValueToString, getValueFromPairPoint
from image_processor import read_image, manipulate_image, save_image


def encryption():
  # Check Validity of Image
  image = None
  image = read_image()

  # Make sure the image is valid
  if (image is not None):
    # Initiate the ECC (ECEG)
    eceg = ECEG()
    print(f"ECC Data:\n a: {eceg.aVal}\n b: {eceg.bVal}\n p: {eceg.pVal}")
    base_point = eceg.getRandomPoint()
    print(f"Base Point: {base_point.getPointNumberValue()} | Hex Value: {base_point.getPointValue()}")

    # User Data
    a_private_key = generatePrimeNumber()
    b_private_key = generatePrimeNumber()
    a_public_key = eceg.multiplyPoint(base_point, a_private_key)
    b_public_key = eceg.multiplyPoint(base_point, b_private_key)

    print(f"\nUser A Data:\n Private Key: {a_private_key}\n Public Key: {a_public_key.getPointNumberValue()} | Hex Value: {a_public_key.getPointValue()}")
    print(f"\nUser B Data:\n Private Key: {b_private_key}\n Public Key: {b_public_key.getPointNumberValue()} | Hex Value: {b_public_key.getPointValue()}")

    # =================
    # =====ENCRYPT=====
    # =================

    # Secret Point
    secret_point = eceg.getRandomPoint()
    k = getKValue(eceg.pVal)
    print(f"\nSecret Point: {secret_point.getPointNumberValue()} | Hex Value: {secret_point.getPointValue()}")
    print(f"K Value: {k}")

    # Determine which public key to use
    used_pub_key_hex = input("Insert the Hex Value of the Public Key to be used: ")
    used_pub_key = Point(0,0)
    used_pub_key.setPointValue(used_pub_key_hex)

    # Encrypt Secret Point
    pair_point = eceg.encryptECEG(k, base_point, secret_point, used_pub_key)
    pair_point_value = getValueFromPairPoint(pair_point)
    encrypted_value = makePairPointValueToString(pair_point_value)
    binary_encrypted_value = makeHexToBin(encrypted_value)
    print("")
    print(f"Encrypted Value Hex: {encrypted_value}")
    print(f"Encrypted Value Bin: {binary_encrypted_value}")
    print(f"Encrypted Value Length: {len(binary_encrypted_value)}")

    # Manipulate Image
    new_image = manipulate_image(image, base_point, binary_encrypted_value)

    # Save Image
    save_image(new_image)