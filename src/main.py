from type.ECEG import ECEG
from utils.number import generatePrimeNumber
from utils.functions import makeNumToHex, makeHexToNum

if __name__ == "__main__":
  incorrectCount = 0
  for i in range (50):
    temp = ECEG()
    print("a: "+temp.aVal+" b: "+temp.bVal +" p: "+temp.pVal)
    
    basePoint = temp.getRandomPoint()
    print("TEMP POINT", basePoint)
    
    aPrivKey = generatePrimeNumber();
    bPrivKey = generatePrimeNumber();

    print("A PRIVATE KEY", aPrivKey, "|", makeNumToHex(aPrivKey))
    print("B PRIVATE KEY", bPrivKey, "|", makeNumToHex(bPrivKey))

    aPubKey = temp.multiplyPoint(basePoint, aPrivKey);
    bPubKey = temp.multiplyPoint(basePoint, bPrivKey);
    
    print("A PUBLIC KEY", aPubKey, "|", aPubKey.getPointValue())
    print("B PUBLIC KEY", bPubKey, "|", bPubKey.getPointValue())

    secretPoint = temp.getRandomPoint()

    print("SECRET POINT", secretPoint, "|", secretPoint.getPointValue())

    k = temp.getKValue()
    
    pairPoint = temp.encryptECEG(k, basePoint, secretPoint, bPubKey)
    decryptedSecretPoint = temp.decryptECEG(bPrivKey, pairPoint)
    print("DECRYPTED SECRET POINT", decryptedSecretPoint, "|", decryptedSecretPoint.getPointValue())

    pairPoint2 = temp.encryptECEG(k, basePoint, secretPoint, aPubKey)
    decryptedSecretPoint2 = temp.decryptECEG(aPrivKey, pairPoint2)
    print("DECRYPTED SECRET POINT 2", decryptedSecretPoint2, "|", decryptedSecretPoint2.getPointValue())

    
    if (secretPoint.getPointValue() == decryptedSecretPoint.getPointValue() and decryptedSecretPoint.getPointValue()  == decryptedSecretPoint2.getPointValue()):
      print("BISAAA SAMA AAWOOAWOAWO")
    else :
      incorrectCount +=1


  print("The incorrect count:", incorrectCount)

