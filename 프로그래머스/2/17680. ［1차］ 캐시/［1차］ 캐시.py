from collections import deque

def solution(cacheSize, cities):
    answer = 0
    arr = deque(maxlen=cacheSize) 

    if cacheSize == 0: 
        return len(cities) * 5

    for i in cities:
        i = i.lower()

        if i in arr: 
            arr.remove(i) 
            arr.appendleft(i) 
            answer += 1
        else: 
            arr.appendleft(i) 
            answer += 5

    return answer
