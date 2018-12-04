#!/usr/local/bin/python3

class Guard():
    def __init__(self, id):
        self.id = id
        self.sleeptimes = [0] * 60

class Roster():
    def __init__(self, inputFile):
        self.logentries = self.__parseInputFile(inputFile)
        self.guards = {}
        self.__countGuardSleep()

    def __parseInputFile(self, inputFile):
        logentries = {}
        import re
        with open(inputFile) as f:
            INPUT = f.read().splitlines()
        for logline in INPUT:
            m = re.match(r'\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] ([ #a-zA-Z0-9]*)', logline)
            timestamp = (int(m.group(2)) * 31 * 24 * 60 + \
                             int(m.group(3)) * 24 * 60 + \
                             int(m.group(4)) * 60 + \
                             int(m.group(5)))
            if m.group(6)[0] == "G":
                event = m.group(6).split()[1].replace("#", "")
            elif m.group(6)[0] == "w":
                event = "W"
            elif m.group(6)[0] == "f":
                event = "F"
            logentries[timestamp] = event
        return logentries

    def __countGuardSleep(self):
        guardid = ""
        startMin = "none"
        while not len(self.logentries) == 0:
            timestamp = min(self.logentries.keys())
            event = self.logentries.pop(min(self.logentries.keys()))
            if not (event == "F") and not (event == "W"):
                guardid = event
            if not (guardid == "") and (event == "F"):
                startMin = timestamp
            if not (guardid == "") and (event == "W"):
                if not int(guardid) in self.guards.keys():
                    self.guards[int(guardid)] = Guard(guardid)
                for i in range(startMin % 60, timestamp % 60):
                    self.guards[int(guardid)].sleeptimes[i] = self.guards[int(guardid)].sleeptimes[i] + 1
                startMin = "none"

    def strategy_one(self):
        # Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
        # What is the ID of the guard you chose multiplied by the minute you chose?
        mostMinutesAsleep = 0
        guardId = None
        sleepiestMinute = None
        for id in self.guards.keys():
            if sum(self.guards[id].sleeptimes) > mostMinutesAsleep:
                mostMinutesAsleep = sum(self.guards[id].sleeptimes)
                guardId = id
                sleepiestMinute = self.guards[id].sleeptimes.index(max(self.guards[id].sleeptimes))
        return guardId * sleepiestMinute

    def strategy_two(self):
        # Of all guards, which guard is most frequently asleep on the same minute?
        # What is the ID of the guard you chose multiplied by the minute you chose?
        mostFrequentlyAsleep = 0
        guardId = None
        sleepiestMinute = None
        for id in self.guards.keys():
            if max(self.guards[id].sleeptimes) > mostFrequentlyAsleep:
                mostFrequentlyAsleep = max(self.guards[id].sleeptimes)
                guardId = id
                sleepiestMinute = self.guards[id].sleeptimes.index(max(self.guards[id].sleeptimes))
        return guardId * sleepiestMinute


roster = Roster("./input.txt")
print("Star 1: %i" % roster.strategy_one())
print("Star 2: %s" % roster.strategy_two())

