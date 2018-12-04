#!/usr/local/bin/python3

class Roster():
    def __init__(self, inputFile):
        self.logentries = self.__parseInputFile(inputFile)
        self.guards = {}
        self.__countGuardSleep()

    def __parseInputFile(self, inputFile):
        logentries = {}
        with open(inputFile) as f: INPUT = f.read().splitlines()
        import re
        for logline in INPUT:
            m = re.match(r'\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] ([ #a-zA-Z0-9]*)', logline)
            ts = (int(m.group(2)) * 31 * 24 * 60 + int(m.group(3)) * 24 * 60 + int(m.group(4)) * 60 + int(m.group(5)))
            if m.group(6)[0] == "G": event = m.group(6).split()[1].replace("#", "")
            elif m.group(6)[0] == "w": event = "W"
            elif m.group(6)[0] == "f": event = "F"
            logentries[ts] = event
        return logentries

    def __countGuardSleep(self):
        gid = ""
        startMin = "none"
        while not len(self.logentries) == 0:
            ts = min(self.logentries.keys())
            event = self.logentries.pop(min(self.logentries.keys()))
            if not (event == "F") and not (event == "W"): gid = event
            if not (gid == "") and (event == "F"): startMin = ts
            if not (gid == "") and (event == "W"):
                if not int(gid) in self.guards.keys(): self.guards[int(gid)] = [0] * 60
                for i in range(startMin % 60, ts % 60): self.guards[int(gid)][i] = self.guards[int(gid)][i] + 1
                startMin = "none"

    def strategy_one(self):
        # Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
        # What is the ID of the guard you chose multiplied by the minute you chose?
        mostMinutesAsleep = 0
        gid = None
        sleepiestMinute = None
        for id in self.guards.keys():
            if sum(self.guards[id]) > mostMinutesAsleep:
                mostMinutesAsleep = sum(self.guards[id])
                gid = id
                sleepiestMinute = self.guards[id].index(max(self.guards[id]))
        return gid * sleepiestMinute

    def strategy_two(self):
        # Of all guards, which guard is most frequently asleep on the same minute?
        # What is the ID of the guard you chose multiplied by the minute you chose?
        mostFrequentlyAsleep = 0
        gid = None
        sleepiestMinute = None
        for id in self.guards.keys():
            if max(self.guards[id]) > mostFrequentlyAsleep:
                mostFrequentlyAsleep = max(self.guards[id])
                gid = id
                sleepiestMinute = self.guards[id].index(max(self.guards[id]))
        return gid * sleepiestMinute


roster = Roster("./input.txt")
print("Star 1: %i" % roster.strategy_one())
print("Star 2: %s" % roster.strategy_two())