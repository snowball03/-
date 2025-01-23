def solution(k, tangerine):
    li = {}
    cnt = 0
    
    for i in tangerine:
        if i in li:
            li[i] += 1
        else:
            li[i] = 1
    
    sort_li = sorted(li.values(), reverse = True)

    for s in sort_li:
        if k <= 0:
            break
        k-= s
        cnt +=1
        
    return cnt