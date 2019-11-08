def solution(record):
    answer = []
    db = {}
    
    for i in record:
        inst = i.split(' ')
        
        if(inst[0]=='Enter'):
            db[inst[1]]=inst[2]
        elif(inst[0]=='Leave'):
            continue
        else: ## inst[0]=='Change'
            db[inst[1]]=inst[2]
            
    for i in record:
        inst = i.split(' ')
        
        if(inst[0]=='Enter'):
            answer.append('{}님이 들어왔습니다.'.format(db[inst[1]]))
        elif(inst[0]=='Leave'):
            answer.append('{}님이 나갔습니다.'.format(db[inst[1]]))
        else: ## inst[0]=='Change'
            continue
    
    return answer