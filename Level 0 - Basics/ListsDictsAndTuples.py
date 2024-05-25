from collections import defaultdict

# Loading list into dict using index as key and elements of list as values
sampleList = [1, 3, 4, 9, 2, 6, 7, 8, 10]
sampleDict = {}
for i in range(0, len(sampleList)):
    sampleDict[i] = sampleList[i]
print(f"Sample Dictionary after loading Sample List: {sampleDict}")

# Returning only the keys from the dictionary
print(f"Here are the keys only: {sampleDict.keys()}")
# This returns the values as dict_keys([0, 1, 2, etc.])
# We need to typecast to list to get back just a list
print(f"Here are the Sample Dictionary keys as a list {list(sampleDict.keys())}")

# Returning the values from the dictionary
print(f"Here are the Sample Dictionary values: {sampleDict.values()}")
# This also needs to be converted to a list to use easily
print(f"Here are the Sample Dictionary values as a list: {list(sampleDict.values())}")

# Returning both keys and values
print(f"Here are the keys and values at once: {sampleDict.items()}")
# This returns an object like a list of tuples and would need to be converted to a list in the same way

# Returning every other value from a list
print(sampleList[0:len(sampleList):2])

# Returning every other value starting with the second value in list
print(sampleList[1:len(sampleList):2])

# Setting up a sample tuple
sampleTuple = tuple(sampleDict.items())
print(sampleTuple)
# This is a tuple of tuples, but it will work for my purposes

# Getting the first item in the tuple
print(sampleTuple[0])

# Getting every other item in the tuple
print(sampleTuple[0:len(sampleTuple):2])

# Loading the tuple of tuples into a new dictionary
newSampleDict = {}
for i, j in sampleTuple:
    newSampleDict[i] = j
print(newSampleDict)

# Creating a list of three-item tuples and loading first into dict as key and latter two as value in dict
threeItemTuplesList = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
threeItemDict = {}
for i, j, k in threeItemTuplesList:
    threeItemDict[i] = (j, k)
print(threeItemDict)

# Trying to convert a tuple to a dict
conversionTuple = (1, 2)
convertedDict = {}
convertedDict[conversionTuple[0]] = conversionTuple[1]
print(convertedDict)