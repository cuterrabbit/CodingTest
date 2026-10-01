def solution(progresses:list[int], speeds:list[int]) -> list[int]:
    answer,deploy_list = [],[]
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        share, mod = divmod(progresses[i], speeds[i])    
        if mod == 0:
            deploy_list.append(share)
        else:
            deploy_list.append(share+1)
    n,m = 0,deploy_list[0]
    for idx,day in enumerate(deploy_list):
        if m >= day:
            n += 1
        else:
            answer.append(n)
            m = day
            n = 1
    answer.append(n)
    return answer