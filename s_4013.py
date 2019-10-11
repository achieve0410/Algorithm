def check(arrs, start, rotation):
    result = [0, 0, 0, 0]
    r_result = [0, 0, 0, 0]

    ## check left
    num = start
    r = rotation
    while(num>0):
        if(num==start):
            result[num-1] = 1
            r_result[num-1] = r
            r *= -1
            num -= 1
        else:
            if(arrs[num-1][2] != arrs[num][6]):
                result[num-1] = 1
                r_result[num-1] = r
                r *= -1
                num -= 1
            else:
                break

    ## check right
    num = start
    r = rotation
    while(num<5):
        if(num==start):
            result[num-1] = 1
            r_result[num-1] = r
            r *= -1
            num += 1
        else:
            if(arrs[num-2][2] != arrs[num-1][6]):
                result[num-1] = 1
                r_result[num-1] = r
                r *= -1
                num += 1
            else:
                break
    return result, r_result

def l_rotation(arrs, rotation):
    if(rotation == 1):
        temp = arrs[7]
        for i in range(7, 0, -1):
            arrs[i] = arrs[i-1]
        arrs[0] = temp
    else:
        temp = arrs[0]
        for i in range(0, 7, 1):
            arrs[i] = arrs[i+1]
        arrs[7] = temp
    return arrs

def solution(arr):
    arrs = arr.copy()
    for i in range(K):
        start, rotation = map(int, input().split())

        result, rot = check(arrs, start, rotation) ## [1, 1, 0, 0], [1, -1, 0, 0]
        for idx, value in enumerate(result):
            if( value==1 ):
                arrs[idx] = l_rotation(arrs[idx], rot[idx])

    return int(arrs[0][0])*1 + int(arrs[1][0])*2 + int(arrs[2][0])*4 + int(arrs[3][0])*8

T = int(input())
arr = [0 for i in range(4)]

for idx in range(T):
    K = int(input())
    for i in range(4):
        arr[i] = input().split()
    answer = solution(arr)
    print("#{} {}".format(idx+1, answer))
