def solution(numbers):
    answer = ''
    
    prep_numbs = []
    
    for num in numbers:
        prep = str(num) * 3
        prep_numbs.append((prep, num))
    
    prep_numbs.sort(reverse=True)
    
    for i,j in prep_numbs:
        answer += str(j)
    
    if answer[0] == '0':
        return '0'
    
    
    return answer