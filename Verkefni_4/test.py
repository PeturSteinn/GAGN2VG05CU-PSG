# func_header = 'TotalTrackCredits'
# argument_list = [9, 9]

# [0] + "SELECT "
# func += '({})'.format(",".join(['{}' for i in range(len(argument_list))])).format(*argument_list)
#func = "SELECT " + func

# print(func)
# xd = ",".join(['{}' for i in range(len(argument_list))])
# print(tmp.format(*argument_list))
# print("SELECT {}")

# print(",".join(list(map(lambda x: str(x), argument_list))))
# func = "SELECT {}".format(tmp.format(",".join(list(map(lambda x: str(x), argument_list))))) # func_header % ",".join(list(map(lambda x: str(x), argument_list)))


#fun += '({})'.format(",".join(['{}' for i in range(len(inp_param))]))
# lul = ",".join(list(map(lambda x: "{" + "{}".format(str(x)) + "}", inp_param)))

# print(func)

import datetime

def generateSemesters():
    start = "2015V"
    end = "{}{}".format(datetime.datetime.now().year + 3, start[-1])
    semesters = [start]
    semester = start

    while(semester != end):
        semester = getNextSemester(semester)
        semesters.append(semester)
    return semesters

def getCurrSemester():
    currDate = datetime.datetime.now()
    if currDate.month > 6: return "{}H".format(currDate.year)
    else: return "{}V".format(currDate.year)

def getNextSemester(sem):
    if sem[-1] == "H": return "{}V".format(int(sem[:-1]) + 1)
    else: return "{}H".format(sem[:-1])

print(generateSemesters())

# print(getNextSemester("2019H"))
# print(getCurrSemester())
