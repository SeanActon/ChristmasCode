
print("Merry Christmas")
import numpy as np
import string

# Read the text file
with open('input.txt', 'r') as f:
  text = f.read()

# Convert the text to an array
array = np.array(text.split())

numbers=['0','1','2','3','4','5','6','7','8','9']
wordNumbers=['one','two','three','four','five','six','seven','eight','nine']
wordNumbersBackwards=['eno','owt','eerht','ruof','xis','neves','thgie','enin']

tmpString=[]
total=0
for number in array:
    tmpString=[]
    for letter in number:
        if letter in numbers:
            tmpString.append(letter)
    currentNumber=int(tmpString[0])*10+int(tmpString[len(tmpString)-1])
    total=total+currentNumber

print ("the result is ")
print(total)
