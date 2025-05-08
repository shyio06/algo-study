def solution(sides):
    sides.sort()
    max_side = sides.pop(2)
    
    if max_side < (sides[0] + sides[1]):
        answer = 1
    else :
        answer = 2
    
    return answer