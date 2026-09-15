def solution(participant, completion):
    
    """
    완주한 사람은 참가자 보다 1 작다 라는 조건
    참가자 중 동명이인 존재. -> 비교 후 break 탈출?
    """
        
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    # 정렬 후 1:1 로 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            
    # participant의 맨 마지막 사람이 미완주자
    return participant[-1]