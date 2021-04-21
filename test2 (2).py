# ~!@#$%^&*
# ~!@#$%^&* 
# ()-_=+

# 8 ≤ password 길이 ≤ 15
# password는 아래 4 종류의 문자 그룹을 제외한, 다른 어떤 문자도 포함해서는 안됩니다.
# [1] 알파벳 대문자(A~Z)
# [2] 알파벳 소문자(a~z)
# [3] 숫자(0~9)
# [4] 특수문자(~!@#$%^&*)
# password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서 3 종류 이상을 포함해야 합니다.
# password에 어떤 문자라도 4개 이상 연속될 수 없습니다.
# password에 어떤 문자라도 5개 이상 포함될 수 없습니다.

# print(ord('A'))65
# print(ord('Z'))90
# print(ord('a'))97
# print(ord('z'))122
# print(ord('~'))126
# print(ord('!'))33
# print(ord('@'))64
# print(ord('#'))35
# print(ord('$'))36
# print(ord('%'))37
# print(ord('^'))94
# print(ord('&'))38
# print(ord('*'))42
# print(ord('('))40
# print(ord(')'))41
# print(ord('-'))45
# print(ord('_'))95
# print(ord('='))61
# print(ord('+'))43
# print(ord('0'))48
# print(ord('9'))57

def test(mystr):
    mystr = ord(mystr)
    if mystr==40 or mystr==41 or mystr==45 or mystr==95 or mystr==61 or mystr==43:
        return False
    elif mystr>=65 and mystr<=90:
        return True
    elif mystr>=97 and mystr<=122:
        return True
    elif mystr>=48 and mystr<=57:
        return True
    elif mystr==126 or mystr==33 or mystr==64 or mystr==35 or mystr==36 or mystr==37 or mystr==94 or mystr==38 or mystr==42:
        return True
    return False

def test2(mystr):
    
    l1 = 0
    l2 = 0
    l3 = 0
    l4 = 0

    for i in mystr:
        i = ord(i)
        if i>=65 and i<=90:
            l1 = 1
        elif i>=97 and i<=122:
            l2 = 1
        elif i==126 or i==33 or i==64 or i==35 or i==36 or i==37 or i==94 or i==38 or i==42:
            l3 = 1
        elif i>=48 and i<=57:
            l4 = 1


    if l1+l2+l3+l4>=3:
        return True
    else:
        return False


def test3(mystr):

    idx = 0
    mych = ''

    for i in mystr:
        if mych!=i:
            mych = i
            idx = 1
        else:
            if(idx==3):
                return False
            else:
                idx += 1
    
    return True

def test4(mystr):

    mydict = {}

    for i in mystr:
        if i not in mydict:
            mydict[i] = 1
        else:
            if mydict[i] >=4:
                return False
            mydict[i] += 1
    
    return True

def solution(inp_str):
    answer = []

    if len(inp_str)<8 or len(inp_str)>15:
        answer.append(1)
    
    for i in inp_str:
        if test(i)==False:
            print(i, test(i))
            answer.append(2)
            break
        else:
            continue
    
    if test2(inp_str)==False:
        answer.append(3)

    if test3(inp_str)==False:
        answer.append(4)  

    if test4(inp_str)==False:
        answer.append(5) 

    if answer == []:
        return [0]
    return answer

print(solution("UUUUU★"))

