def solution(s):
    s_list = list(s)
    
    # top check
    if s_list[-1] == '(':
        return False
    
    # pair check
    n, m = 0, 0
    for str in s_list:
        if str == '(':
            n += 1
        else:
            m += 1
    if n != m:
        return False
    
    # 올바른 괄호
    stack = []
    for str in s_list:
        if str == '(':
            stack.append(')')
        elif not stack or stack.pop() != str:
            return False
        
    return not stack