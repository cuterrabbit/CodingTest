def solution(s):
    
    stack = []
    
    for p in s:
        stack.append(p)
    
    sum = 0
    
    while len(stack) > 0:
        if stack.pop() == ')':
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            return False
    
    if sum == 0:
        return True
    else:
        return False