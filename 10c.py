sampleDict = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Maximum Value in Dictionary : ', itemMaxValue[1])
listOfKeys = list()
for key, value in sampleDict.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)
print('Keys with maximum Value in Dictionary : ', listOfKeys)
