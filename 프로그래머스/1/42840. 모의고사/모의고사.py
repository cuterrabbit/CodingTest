def solution(answers):
    answer = []
    list1, list2, list3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    len1, len2, len3, len_answers = 5, 8, 10, len(answers)
    share1, mod1 = divmod(len_answers, len1)
    if share1 == 0:
        pass
    else:
        list1 *= share1
        for i in range(mod1):
            list1.append(list1[i])
    
    share2, mod2 = divmod(len_answers, len2)
    if share2 == 0:
        pass
    else:
        list2 *= share2
        for i in range(mod2):
            list2.append(list2[i])
        
    share3, mod3 = divmod(len_answers, len3)
    if share3 == 0:
        pass
    else:
        list3 *= share3
        for i in range(mod3):
            list3.append(list3[i])
    
    n,m,l = 0,0,0
    for i in range(len_answers):
        if answers[i] == list1[i]:
            n += 1
        if answers[i] == list2[i]:
            m += 1
        if answers[i] == list3[i]:
            l += 1
    max_score = max(n,m,l)
    if n == max_score:
        answer.append(1)
    if m == max_score:
        answer.append(2)
    if l == max_score:
        answer.append(3)
    
    return answer