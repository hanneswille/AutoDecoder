
import re
import sys
import base64
import base58
import codecs
from numpy import outer
from guess_language import guess_language




def runFullArray(inputstring):
    for i in range(len(decoderArray)):
        decodedString = decode(inputstring, decoderArray[i])
        result = substituteToRealtext(decodedString)
        if result != None:
            english = False
            #print(result + " With method used " + decoderArray[i])
            english = checkEnglish(result.lower())
            decoding= Decoding()
            decoding.method = decoderArray[i]
            decoding.initialResult = decodedString
            decoding.englishResult = result.lower()
            if english:
                outputEng.append(decoding)
            else:
                outputNotEng.append(decoding)
        else:
            outputFalse.append(decoderArray[i])
            #print("Method " + decoderArray[i] + " was not valid")


def decode(inputstring, method):
    res = ""
    try:
        if method == "Base64":
            res = base64.b64decode(inputstring).decode()
        elif method == "Base32":
            res = base64.b32decode(inputstring).decode()
        elif method == "Base58":
            res = base58.b58decode(inputstring).decode()
        elif method == "Rot13":
            res = codecs.encode(inputstring, 'rot13')
        return res
    except:
        return res
        
    

def substituteToRealtext(decodedString):
    newstring = ""
    if len(decodedString) >=1:
        #Normal substitution
        for char in decodedString:
            if char in substitutionDict.keys():
                newstring+= substitutionDict.get(char)
            else:
                newstring+= char     

        return newstring
    else:
        return None


def checkEnglish(input):
    if guess_language(input) == "en":
        return True
    else:
        return False
    
    
def printOutput():
    print("THE ATTEMPTS THAT LOOK ENGLISH ARE:")
    for i in range(len(outputEng)):
        print(""+outputEng[i].getMethod() +" With initial result " + outputEng[i].getInitial() + " and final output of " + outputEng[i].getEnglish())
    print("============================================")
    print("THE GUESSES THAT COULD POTENTIALLY BE VALID:")
    for i in range(len(outputNotEng)):
        print(""+outputNotEng[i].getMethod()+" With initial result " + outputNotEng[i].getInitial() + " and final output of " + outputNotEng[i].getEnglish())
    print("============================================")
    print("THESE ENCODING SCHEMES DO NOT PRODUCE VALID OUTCOMES")
    for i in range(len(outputFalse)):
        print(outputFalse[i])
    
class Decoding:
    method = ""
    initialResult= ""
    englishResult = ""
    def getMethod(self):
        return self.method
    def getInitial(self):
        return self.initialResult
    def getEnglish(self):
        return self.englishResult
    
#initial variables
inputstring = ""
method = ""
resultSubst = ""
decoderArray = ["Base64", "Base58", "Base32", "Rot13"]
substitutionDict = {"0":"O","1":"I","3": "E", "4": "A", "5":"S", "-": " ", "_": " ", "€": "E", "7": "T", "@":"A" }
specialCase= {"!": "I"} #not on end of string
outputEng = []
outputNotEng = []
outputFalse = []



#Main function
if len(sys.argv) == 2:
    runFullArray(sys.argv[1])
elif len(sys.argv) == 3:
    decode(sys.argv[1], sys.argv[2])
else:
    print("To many arguments Or none")
    sys.exit()
printOutput()
