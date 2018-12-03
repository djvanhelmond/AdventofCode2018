#!/usr/local/bin/python3

class Claim():
    def __init__(self, claimStr):
        import re
        m = re.match( r'#([0-9]*) @ ([0-9,]*): ([0-9x]*)', claimStr)
        self.ID = int(m.group(1))
        self.pos = map(int, m.group(2).split(","))
        self.size = map(int, m.group(3).split("x"))
        self.absList = []
        for x in range(self.pos[0], self.pos[0] + self.size[0]):
            for y in range(self.pos[1], self.pos[1] + self.size[1]):
                self.absList.append(str(x) + "x" + str(y))


class Fabric():
    def __init__(self, inputFile):
        self.claimList = self.__parseInputFile(inputFile)
        self.claimedfabric = {}
        self.__processClaims()

    def __parseInputFile(self, inputFile):
        with open(inputFile) as f: INPUT = f.read().splitlines()
        claimList = [Claim(claim) for claim in INPUT]
        return claimList

    def __processClaims(self):
        for claim in self.claimList:
            for piece in claim.absList:
                if piece in self.claimedfabric:
                    self.claimedfabric[piece] = self.claimedfabric[piece] + 1
                else:
                    self.claimedfabric[piece] = 1

    def countDoubles(self):
        doubles = 0
        for claimedpiece in self.claimedfabric:
            if not self.claimedfabric[claimedpiece] == 1:
                doubles += 1
        return doubles

    def findNonOverlappingClaim(self):
        uniqueList = []
        for claim in self.claimList:
            unique = True
            for piece in claim.absList:
                if not self.claimedfabric[piece] == 1:
                    unique = False
            if unique:
                uniqueList.append(claim.ID)
        return uniqueList



fabric = Fabric("./input.txt")
print("Star 1: %i" % fabric.countDoubles())
print("Star 2: %s" % fabric.findNonOverlappingClaim())

