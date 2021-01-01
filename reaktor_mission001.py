import base64
import re

f = open("input.txt", "r")
data = f.read()

NO_OF_CHARS = 256
  
# Returns an array of size 256 containg count 
# of characters in the passed char array 
def getCharCountArray(string): 
    count = [0] * NO_OF_CHARS 
    for i in string: 
        count[ord(i)]+= 1
    return count

def noRepeating(string): 
    count = getCharCountArray(string)
    for i in string: 
        if count[ord(i)] > 1: 
            return False
    return True

def decodeAndPrint(idata):
    try:
        if noRepeating(idata):
            print(idata)
            decode = base64.b64decode(idata.encode())
            print(decode)
        return True
    except:
        return False

idx = 0
for d in list(data):
    decode = d
    if idx+16 < len(data):
        for i in range(1, 16):
            decode+=list(data)[idx+i]
        decodeAndPrint(decode)
    idx+=1

print('done.')
