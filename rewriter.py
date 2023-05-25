finalArray = []
f = open('input.txt', 'r')
inputString = f.read()
tempArray = inputString.splitlines()
for i in range(0, len(tempArray)):
    splittedTempArray = tempArray[i].split(" ", 1)
    finalArray.append(splittedTempArray[0])

for i in range(0, len(finalArray)): 
    if finalArray[i] != 'webdriver-manager' and finalArray[i] != 'selenium' and finalArray[i] != 'selenium-wire' and finalArray[i] != 'tk':
        with open('output.txt', 'a') as f:
            f.write('--exclude-module ' + finalArray[i] + ' ')
