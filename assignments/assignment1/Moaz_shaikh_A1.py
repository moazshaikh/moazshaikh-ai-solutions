# IT 209 Assignment 1 by Moaz Shaikh
# Specs: Assignment specified to read a file and display individual items spaced out. Then we were
# asked to build a dictionary and write its values on separate lines to a new text file
# Separate functions performed the different jobs

def loadItems():
    fname = 'stateinfo7.txt'
    f = open(fname, 'r')
    stateLines = f.readlines()
    f.close()
    stateList = []
    for state in stateLines:
        line = state.split(';')
        if len(line) > 1:
            line = [n.strip() for n in line]
        stateList.append(line)
    return stateList


def displayItems(stateList):
    stateList.sort()
    for state in stateList:
        print(state[0] + '     ' + state[1] + '     ' + state[2] + '     ' + state[3] + '\n')

def buildDict(stateList):
    newDict = {}
    for state in stateList:
        newDict[state[0]] = [state[1], state[2], state[3]]
    return newDict

def writeFile(stateDict):
    f = open('IT209_A1output.txt', 'w')
    for state in stateDict:
        placeholderList = stateDict[state]
        f.write(placeholderList[0] + ',' + placeholderList[1] + ',' +placeholderList[2] + '\n')


stateList1 = loadItems()
displayItems(stateList1)
SD = buildDict(stateList1)
writeFile(SD)
