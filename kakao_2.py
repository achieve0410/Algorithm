import operator

def solution(N, stages):
    answer = []
    arrive = [0 for i in range(N+1)]
    fail = [0 for i in range(N+1)]
    
    failure = {}
    
    for n in range(1, N+1, 1):
        for stg in stages:
            if(stg == N+1):
                arrive[n] += 1
            else:
                if(stg >= n):
                    arrive[n] += 1
                if(stg == n):
                    fail[n] += 1
                
    for n in range(1, N+1, 1):
        if(arrive[n]!= 0):
            failure[n] = fail[n] / arrive[n]
        if(arrive[n]==0):
            failure[n] = 0
    
    # print(failure)
    failure = dict(sorted(failure.items(), key=operator.itemgetter(1), reverse=True))
    answer = list(failure.keys())
    # print(failure)
        
    
    return answer