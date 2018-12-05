#!/usr/local/bin/python3

class Polymer():
    def __init__(self, inputFile, brokenUnit):
        self.chain = self.__parseInputFile(inputFile)
        if not brokenUnit == None:
            self.chain = self.__removeBroken(brokenUnit)
        while self.__findReaction():
            pass

    def __parseInputFile(self, inputFile):
        with open(inputFile) as f:
            return list(f.read().splitlines()[0])

    def __removeBroken(self, brokenUnit):
        newchain = []
        for pos in range(len(self.chain)):
            if not ((self.chain[pos] == brokenUnit) or (self.chain[pos] == brokenUnit.swapcase())):
                newchain.append(self.chain[pos])
        return newchain

    def __findReaction(self):
        for pos in range(len(self.chain) - 1):
            if self.chain[pos] == self.chain[pos + 1].swapcase():
                self.chain.pop(pos)
                self.chain.pop(pos)
                return True
        return False


polymer = Polymer("./input.txt", None)
print("Star 1: %i" % len(polymer.chain))

star2 = {}
for char in range(97, 123):
    polymer = Polymer("./input.txt", chr(char))
    star2[chr(char)] = len(polymer.chain)
print("Star 2: %s %i" % (min(star2, key=star2.get), star2[min(star2, key=star2.get)]))
