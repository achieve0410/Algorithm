def rotation(num):
    arr = num
    length = len(arr)

    temp = arr[length-1]
    for i in range(length-1, 0, -1):
        arr[i] = arr[i-1] 
    arr[0] = temp

    return arr

def add_num(num, num_dict):
    ret_dict = num_dict
    length = len(num)
    num_length = length//4

    for i in range(4):
        t_num = str("".join(num[num_length*i:num_length*(i+1)]))
        if(t_num not in ret_dict):
            ret_dict[t_num] = 1
        else:
            continue
    return ret_dict

def solution(num, K):
    num_dict = {}
    num_length = len(num)//4

    for _ in range(num_length):
        num_dict = add_num(num, num_dict)
        rotation(num)

    return sorted(num_dict.items(), reverse=True)

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    num = list(map(str, input()))

    answer = solution(num, K)
    print("#{} {}".format(i+1, int(answer[K-1][0], 16)))