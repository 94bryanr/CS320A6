import sys
sys.setrecursionlimit(20000)

# Get our coin set
stringCoinSet = open("coins", "r").readline().strip().split(' ')
# Convert to integers
coinSet = []
for stringCoin in stringCoinSet:
    coinSet.append(int(stringCoin))

# Get the change we must give back
change = int(sys.argv[1])

# Recursive Programming Solution
# (2,1) is the same as (1,2)
# Inductive step: Return change left - coin
# Base case: Change left is negative or 0
#   If 0: Return coin set
#   If negative: Invalid coin set

def findCoinSet(changeLeft, low, high):
    if (changeLeft < 0):
        return
    if (changeLeft == 0):
        global numberOfCombinations
        numberOfCombinations += 1
        return
    for x in range(low, high):
        global coinSet
        newChangeLeft = changeLeft - (int(coinSet[x]))
        if (newChangeLeft >= 0):
            global numRecursiveCalls
            numRecursiveCalls += 1
            findCoinSet( newChangeLeft, x, high )
        else:
            break


numRecursiveCalls = 0
numberOfCombinations = 0
high = len(coinSet)
findCoinSet(change, 0, high)
print "Change: " + str(change) 
print "Coin Set: " + str(stringCoinSet) 
print "Combinations: " + str(numberOfCombinations)
print "Recursive Calls: " + str(numRecursiveCalls)
