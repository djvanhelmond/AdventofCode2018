#!/usr/local/bin/python3

class Polymer():
    def __init__(self, inputFile, brokenUnit):
        with open(inputFile) as f:
            self.chain = list(f.read().splitlines()[0])
        if not brokenUnit == None:
            newchain = []
            for pos in range(len(self.chain)):
                if not ((self.chain[pos] == brokenUnit) or (self.chain[pos] == brokenUnit.swapcase())):
                    newchain.append(self.chain[pos])
            self.chain = newchain
        while self.__findReaction():
            pass

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
