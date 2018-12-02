#!/usr/local/bin/python3

class Box():
    def __init__(self, ID):
        from collections import Counter
        self.ID = ID
        occurrences = dict(Counter(self.ID)).values()
        if 2 in occurrences: self.twoLetters = True
        else: self.twoLetters = False
        if 3 in occurrences: self.threeLetters = True
        else: self.threeLetters = False

    def __isExactOneCharOff(self, otherID):
        CharOff = 0
        i = 0
        while (CharOff <= 1) and (i < len(self.ID)):
            if not (self.ID[i] == otherID[i]): CharOff += 1
            i += 1
        return CharOff == 1

    def findOffByOneBox(self, boxList):
        for box in boxList:
            if self.__isExactOneCharOff(box.ID):
                return box.ID
        return False





class WareHouse():
    def __init__(self, inputFile):
        self.boxes  = self.__parseInputFile(inputFile)

    def __parseInputFile(self, inputFile):
        with open(inputFile) as f: INPUT = f.read().splitlines()
        boxList = []
        for id in INPUT:
            boxList.append(Box(id))
        return boxList

    def calcChecksum(self):
        twos = 0
        threes = 0
        for box in self.boxes:
            if box.twoLetters:
                twos += 1
            if box.threeLetters:
                threes += 1
        return twos * threes

    def findProto(self):
        for box in self.boxes:
            offBox = box.findOffByOneBox(self.boxes)
            if offBox:
                common = []
                for i in range(len(offBox)):
                    if box.ID[i] == offBox[i]:
                        common.append(offBox[i])
        return ''.join(common)


warehouse = WareHouse("./input.txt")
print("Star 1: %i" % warehouse.calcChecksum())
print("Star 2: %s" % warehouse.findProto())

