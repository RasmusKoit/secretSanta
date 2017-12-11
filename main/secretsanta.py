def readFileToList(filename):
    list = []
    with open(filename, "r") as file:
        for line in file:
            list.append(line.rstrip())
        file.close()
    return list


def generateNames(mainlist):
    from random import choice
    finalList = []
    tempList = mainlist[:]
    check = True
    writeToFile("[Teeb kingi]: [Saab kingi]")
    for name in mainlist:
        while check:
            SSName = choice(tempList)
            if name != SSName:
                string = name + ": " + SSName
                finalList.append(string)
                writeToFile(string)
                check = False
                tempList.remove(SSName)
        check = True
    return finalList


def writeToFile(string):
    with open("secretSanta.txt", "a") as f:
        f.write(string + '\n')
    f.close()


if __name__ == '__main__':
    nameList = readFileToList("nimed.txt")
    print(nameList)
    SSList = generateNames(nameList)
