#!/usr/local/bin/python3

class TimeDevice():

    def __init__(self, inputFile):
        self.freq = 0
        self.freqChangeList = self.__parsefreqChangeList(inputFile)
        self.seenBefore = [ self.freq ]
        self.__run()

    def __parsefreqChangeList(self, inputFile):
        with open(inputFile) as f: INPUT = f.read().splitlines()
        return map(int, INPUT)

    def __run(self):
        from itertools import cycle
        circleList = cycle(self.freqChangeList)
        seen = False
        while not seen:
            self.freq = self.freq + circleList.next()
            if self.freq not in self.seenBefore:
                self.seenBefore.append(self.freq)
            else:
                seen = True



timedevice = TimeDevice("./input.txt")

print("Star 1: %i" % sum(timedevice.freqChangeList))
print("Star 2: %i" % timedevice.freq)
