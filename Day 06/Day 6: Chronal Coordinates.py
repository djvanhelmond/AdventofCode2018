#!/usr/local/bin/python3

d = False

class Chronal():
    def __init__(self, inputFile):
        self.places = self.__parseInputFile(inputFile)
        self.width = max([ int(x[0]) for x in self.places.values()]) + 2
        if d: print(self.width)
        self.height = max([ int(x[1]) for x in self.places.values()]) + 2
        if d: print(self.height)
        self.safeRegionBoundary = 10000
        self.safeRegionSize = 0
        self.grid = {}
        self.__calcLowestManhattanForEachGridLocation()
        self.areas = self.__calcAreas()
        self.__removeInfinites()
        if d: print(self.areas)

    def __parseInputFile(self, inputFile):
        with open(inputFile) as f:
            coors = [ x.split(", ") for x in f.read().splitlines() ]
        coordict = {}
        for i in range(len(coors)):
            coordict[i + 65] = coors[i]
        return coordict


    def __calcLowestManhattanForEachGridLocation(self):
        for y in range(self.height):
            for x in range(self.width):
                mDist = {}
                for p in self.places:
                    mDist[p] = abs(int(self.places[p][0])-x) + abs(int(self.places[p][1])-y)
                    if d: print(x, y, p, self.places[p])
                if d: print("mDist")
                if d: print(mDist)
                if d: print(x, y, sum(mDist.values()))
                if sum(mDist.values()) < self.safeRegionBoundary:
                    self.safeRegionSize = self.safeRegionSize + 1
                if d: print(mDist.values().index(min(mDist.values())))
                closestPlaces = [ place for place, distance in mDist.items() if distance == min(mDist.values()) ]
                if d: print(closestPlaces)
                if len(closestPlaces) == 1:
                    self.grid[str(x)+"x"+str(y)] = closestPlaces[0]
                else:
                    self.grid[str(x) + "x" + str(y)] = 46

    def __calcAreas(self):
        areas = {}
        if d: print("=self.places=")
        if d: print(self.places)
        if d: print("=self.grid=")
        if d: print(self.grid)
        for p in self.places.keys():
            areas[p] = len([grid for grid, closestPlace in self.grid.items() if closestPlace == p])
        if d: print("=areas=")
        if d: print(areas)
        return areas

    def __removeInfinites(self):
        popList = []
        for x in range(self.width):
            y = 0
            if (self.grid[str(x)+"x"+str(y)] in self.areas.keys()) and (self.grid[str(x)+"x"+str(y)] not in popList):
                popList.append(self.grid[str(x)+"x"+str(y)])
        for x in range(self.width):
            y = self.height - 1
            if (self.grid[str(x)+"x"+str(y)] in self.areas.keys()) and (self.grid[str(x)+"x"+str(y)] not in popList):
                popList.append(self.grid[str(x)+"x"+str(y)])
        for y in range(self.height):
            x = 0
            if (self.grid[str(x)+"x"+str(y)] in self.areas.keys()) and (self.grid[str(x)+"x"+str(y)] not in popList):
                popList.append(self.grid[str(x)+"x"+str(y)])
        for y in range(self.height):
            x = self.width - 1
            if (self.grid[str(x)+"x"+str(y)] in self.areas.keys()) and (self.grid[str(x)+"x"+str(y)] not in popList):
                popList.append(self.grid[str(x)+"x"+str(y)])

        if d: print("=popList=")
        if d: print(popList)
        for p in popList:
            self.areas.pop(p)










    def printGrid(self):
        for y in range(self.height):
            line = []
            for x in range(self.width):
                if str(x)+"x"+str(y) in self.grid.keys():
                    line.append(chr(self.grid[str(x)+"x"+str(y)]))
                else:
                    line.append(".")
            print("".join(line))





chronal = Chronal("./input.txt")
if d: chronal.printGrid()

print("Star 1: %i" % (max(chronal.areas.values())))
print("Star 2: %s" % chronal.safeRegionSize)

