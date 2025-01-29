def solution(brown, yellow):
    answer = []
    tmo = []
    total = brown + yellow
    
    for width in range(1, int(total **0.5) +1):
        if total % width == 0: 
            height = total // width
            
            if (width-2) * (height -2) == yellow:
                return [max(width, height), min(width, height)]
