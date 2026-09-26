def solution(citations):
    answer = 0
    
    h_cita = []
    m = max(citations)
    
    for i in range(m + 1):
        n = 0 
        for citation in citations:
            if i <= citation:
                n += 1
        h_cita.append(n)
    
    for idx, h_index in enumerate(h_cita):
        if idx <= h_index:
            answer = idx  
    
    return answer  