
def solution(num, M):
    answer = []
    max_num = max(num)

    a, b = 0, 1
    for i in range(max_num):
        a, b = b, (a+b)%M
        if((i+1) in num):
            answer.append(a)

    return answer

if(__name__=='__main__'):
    Q, M = list(map(int, input().split()))
    num = []

    for i in range(Q):
        num.append(int(input()))

    answer = solution(num, M)
    for i in answer:
        print(i, end='\n')