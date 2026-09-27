def solution(citations):
    answer = 0
    papers = []
    citations.sort()
    for h in range(citations[-1]+1):
        n = 0
        for citation in citations:
            if h <= citation:
                n += 1
        papers.append(n)
            
    for idx,paper in enumerate(papers):
        if idx <= paper:
            answer = idx
        
    return answer  