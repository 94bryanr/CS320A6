import sys
import numpy
sys.setrecursionlimit(20000)

# Get our coin set
stringCoinSet = open("coins", "r").readline().strip().split(' ')
# Convert to integers
coinSet = []
for stringCoin in stringCoinSet:
    coinSet.append(int(stringCoin))
# Get the change we must give back
change = int(sys.argv[1])

# Matrix (-1) means the value has not been defined
high = len(coinSet)
array = numpy.full((change + 1, high), -1)
def findCoinSet(changeLeft, low, high):
    callTotal = 0
    # Search for (changeLeft, low)
    if (array[changeLeft, low] != -1):
        return array[changeLeft, low]
    if (changeLeft < 0):
        return 0
    if (changeLeft == 0):
        return 1
    for x in range(low, high):
        global coinSet
        newChangeLeft = changeLeft - (int(coinSet[x]))
        if (newChangeLeft >= 0):
            combinationsFound = findCoinSet( newChangeLeft, x, high )
            callTotal += int(combinationsFound)
        else:
            break
    # Set matrix index (changeLeft, low) to callTotal
    array[changeLeft][low] = int(callTotal)
    return callTotal

total = findCoinSet(change, 0, high)

print "Change: " + str(change) 
print "Coin Set: " + str(stringCoinSet) 
print "Matches: " + str(total)

