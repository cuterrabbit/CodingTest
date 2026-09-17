def solution(array, commands):
    answer = []
    
    for arr in commands:
        i, j, k = arr[0], arr[1], arr[2]
        
        array_cutting = []
        
        for n in range(i-1, j):
            array_cutting.append(array[n])
        
        array_cutting.sort()
        answer.append(array_cutting[k-1])

        
    
    return answer