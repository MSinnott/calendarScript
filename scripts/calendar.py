#Main calendar program; displays calendar events

#Colors
BLACK   = 30
RED     = 31
DGREEN  = 32
YELLOW  = 33
BLUE    = 34
PURPLE  = 35
LGREEN  = 36
WHITE   = 37

class Event:
    def __init__(self, title, startTime, endTime, desc = ""):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.desc = desc

    def getTimeDifference(self):
        return abs(self.startTime - self.endTime)
    
    def contains(self, otherTime):
        return self.startTime <= otherTime and self.endTime >= otherTime

#This method is just to display all possible formatting -- it is not important
def print_format_table():
    for style in range(8):
        for fg in range(30,38):
            s1 = ""
            for bg in range(40, 48):
                format = ";".join([str(style), str(fg), str(bg)])
                s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
            print(s1)
        print "\n"

#prints @text in @fgcolor and @bgcolor
def cprint(text, fgcolor, bgcolor):
    colorStr = "1;" + str(fgcolor) + ";" + str(bgcolor+10)
    print "\x1b[" + colorStr + "m" + text + "\x1b[0m"

def frange(start, stop, step = 1):
    res = []
    curr = start
    while curr < stop:
        res.append(curr)
        curr += step
    return res
    
import sys
currentTime = 4.75

events = []

events.append(Event("Gaming Club", 8, 12))
for i in frange(currentTime, 12.0, .25):
    eline = ""
    for event in events:
        if(event.contains(i)):
            cprint(event.title + " @ " + str(i) + "\t", BLACK, PURPLE)
        else:
            cprint("\t\t\t", YELLOW, YELLOW)
