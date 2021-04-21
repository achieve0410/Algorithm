
# print(ord('0'))48
# print(ord('9'))57
# print(ord('A'))65
# print(ord('Z'))90
# print(ord('a'))97
# print(ord('z'))122

#print(isinstance(_string, str))

# def test1(mystr):

def checkstr(argu):

    num = 0
    st = 0
    
    num_str = 0
    num_num = 0

    for arg in argu:
        # print("prt arg", arg)
        for i in range(len(arg)):
            myarg = ord(arg[i])
            # print(myarg)

            if myarg>=48 and myarg<=57:
                if st == 1:
                    return 'FALSE'
                if num == 1:
                    continue
                else:
                    num = 1
            elif (myarg >=65 and myarg<=90) or (myarg >=97 and myarg<=122):
                if num == 1:
                    return 'FALSE'
                if st == 1:
                    continue
                else:
                    st = 1
    
        if st == 1:
            if num_str >= 1:
                return 'FALSE'
            else:
                num_str += 1
        elif num == 1:
            num_num += 1
        else:
            return 'FALSE'
    
    if num_str == 1:
        return 'STRING'
    elif num_num >= 1:
        return 'NUMBERS'
    else:
        return 'FALSE'


def solution(program, flag_rules, commands):
    answer = []

    # print("rules: ", flag_rules)
    # print("commands: ", commands)
    myruledict = {}

    for flag_rule in flag_rules:
        mystr = ""
        myflag = ""
        myarg = ""
        myalias = 0

        for i in range(len(flag_rule)):
            # print(mystr, myflag, myarg, myalias)

            if flag_rule[i]==" ":

                if myalias == 1:
                    myruledict[myflag] = myruledict[mystr]

                if mystr[0] == '-':
                    myflag = mystr
                    myarg = 'NULL'
                    myruledict[myflag] = myarg
                elif mystr == 'ALIAS':
                    myalias = 1
                    continue
                else:
                    myarg = mystr
                    myruledict[myflag] = myarg
                mystr = ""
            else:
                mystr += flag_rule[i]

        print(mystr, myflag, myarg, myalias)
        if myalias == 1:
            if mystr[5:] not in myruledict:
                myruledict[mystr[5:]] = ''
            else:
                myruledict[myflag] = myruledict[mystr[5:]]
        elif mystr[0] == '-':
            myflag = mystr
            myarg = 'NULL'
            myruledict[myflag] = myarg
        else:
            myarg = mystr
            myruledict[myflag] = myarg

    for command in commands:
        mystr = ""
        myprog = ""
        myflag = ""
        myarg = ""
        mydict = {}
        # print(command)

        myidx = 0

        for i in range(len(command)):
            if command[i]==" ":
                if myidx == 0:
                    myprog = mystr
                    # print("myprog")
                    myidx = 1
                    mystr=""
                elif mystr[0]=='-':
                    myflag = mystr
                    # print("myflag")
                    if myflag not in mydict:
                        mydict[myflag] = []
                    mystr=""
                    myarg=""
                else:
                    myarg = mystr
                    # print("myarg")
                    mydict[myflag].append(myarg)
                    mystr=""
                
                # print("1:", myprog, "2:", myflag, "3:", myarg)

            else:
                mystr += command[i]
                # print(mystr)
            
            if i==len(command)-1:
                if mystr[0]=='-':
                    myflag = mystr
                    # print("myflag")
                    if myflag not in mydict:
                        mydict[myflag] = []
                    mystr=""
                    myarg=""
                else:
                    myarg = mystr
                    # print("myarg")
                    mydict[myflag].append(myarg)
                    mystr=""                
        
        print("mydict:", mydict)
        print("myruledict: ", myruledict)

        if myprog not in program:
            # print("not prog")
            # print('False1')
            answer.append(False)
            continue
        else:
            for flag, arg in mydict.items():
                tmp = 0
                # print(flag, arg)
                # print(checkstr(arg))

                if flag in myruledict:
                    if myruledict[flag] == 'STRING':
                        if checkstr(arg) == 'STRING':
                            continue
                        else:
                            tmp = 1
                            # print('False2')
                            answer.append(False)
                            break
                    elif myruledict[flag] == 'NUMBERS':
                        if checkstr(arg) == 'NUMBERS':
                            continue
                        else:
                            tmp = 1
                            # print('False3')
                            answer.append(False)
                            break
                    elif myruledict[flag] == 'NULL':
                        continue
                else:
                    tmp = 1
                    # print('False4')
                    answer.append(False)
                    break

            if tmp == 0:
                # print('True5')
                answer.append(True)
                continue

    return answer

# print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e -t 100", "lien -s Bye"])) ## [False, False]
# print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"])) ## [True, False]
# print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"])) ## [True, False]
# print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])) ## [True, False]
# print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"])) ## [True, False]
print(solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"])) ## [True, False]
print(solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"])) ## [True, False]