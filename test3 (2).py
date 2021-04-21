

def rule1(mydict):
    return

def rule2(mydict):
    return

def rule3(mydict):
    return

def solution(data, word):
    answer = []
    mydict = {}
    filedict = {}

    for i in data:
        myid, name, par = i.split(' ')
        myid = int(myid)
        par = int(par)

        if par == 0:
            mydict[myid] = []
            filedict[myid] = [name]
        else:
            if par not in mydict:
                mydict[par] = [myid]
                filedict[par] = [name]
            else:
                mydict[par].append(myid)
                filedict[par].append(name)

    print(mydict)
    print(filedict)

    ## rule 1


    ## rule 2

    
    ## rule 3


    return answer





print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"], "BROWN"))