#Short script that breaks a short event into date, name, etc

import sys

Months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
Days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]

dateRegex = ["##/##/####", "#/#/####", "##/#/####", "#/##/####"]
timeRegex = ["##:##am", "##:##pm", "#:##am", "#:##pm", "##:##", "#:##", "##am", "##pm", "#am", "#pm"]

for m in Months:
    dateRegex.append(m + " ##, ####")
    dateRegex.append(m + " #, ####")
    for d in Days:
        dateRegex.append(d + ", " + m + " ##")
        dateRegex.append(d + ", " + m + " #")

#Uses a regular expression to find a date / time
def exprAt(str, expr, ind = 0):
    for j in range(len(expr)):	
        if expr[j:j+1] == "#":
            if not str[ind+j:ind+j+1].isdigit():
	        return ""
	elif not expr[j:j+1] == str[ind+j:ind+j+1]:
	    return ""
    return [str[ind:ind+len(expr)] , ind, ind + len(expr)]

#Gets all of the dates
def getAllRegex(str, regex):
    results = []
    stindecies = []
    endindecies = []
	
    ind = 0
    while ind < len(str):
        for expr in regex:
	    res = exprAt(str, expr, ind)
	    if not res == "":
	        results.append(res[0])
	        stindecies.append(res[1])
	        endindecies.append(res[2])
                ind = res[2]
        ind +=1
    if len(results) > 0:
        return [results, stindecies, endindecies]
    return ""

def condenseNewlines(str):
    ret = []
    for arg in argList:
        if not arg == "\n":
	    ret.append(arg)
    return ret

def arrToStr(arr):
    ret = ""
    for elem in arr:
        ret += elem
    return ret

argList = sys.stdin.readlines()

argList = condenseNewlines(argList)

titles = []
descs = []
dates = []
times = [[]]

buf = []
for arg in argList:
    date = getAllRegex(arg, dateRegex)
    time = getAllRegex(arg, timeRegex)
    if not date == "":
        titles.append(buf[len(buf) - 1])
	descs.append(arrToStr(buf[:len(buf)-1]))
	dates.append(date)
	times.append([])
	buf = []
	
    if not time == "":
	times[len(times) - 1].append(time)
	
    buf.append(arg)	

descs = descs[1:]		
descs.append(arrToStr(buf[:len(buf)-2]))

times = times[1:]

events = []
for i in range(len(titles)):
    events.append([titles[i], dates[i], times[i], descs[i]])
    print ""
    print events[i]

exit()
