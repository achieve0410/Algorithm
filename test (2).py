import operator
def solution(table, languages, preference):
    # answer = ''
    defi = ['SI', 'CONTENTS', 'HARDWARE', 'PORTAL', 'GAME']
    
    mydict = {}
    
    for i in table:
        mystr = ""
        lan = ""
        myidx = 5
        for j in range(len(i)):
            if(i[j]==' '):
                if mystr in defi:
                    if mystr not in mydict:
                        mydict[mystr]=0
                        lan = mystr
                        mystr = ""
                    continue
                else:
                    if mystr in languages:
                        lan_idx = languages.index(mystr)
                        mydict[lan] += myidx * preference[lan_idx]
                    mystr = ""
                    myidx -= 1
            else:
                mystr += i[j]
        if mystr in languages:
            lan_idx = languages.index(mystr)
            mydict[lan] += myidx * preference[lan_idx]
            mystr = ""
            myidx -= 1

    ky = "Z"
    mx = 0
    for key, value in mydict.items():
        if(value>=mx):
            mx = value
            if(key[0]<=ky):
                answer = key

    return answer




solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["JAVA", "JAVASCRIPT"], [7, 5])