class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        answer_list = []

        s_list=list(s)
        p_list=list(p)
        p_list.sort()
        
        for i in range(len(s) - len(p) + 1):
            sort_prep_s = s_list[i:i+len(p)]
            sort_prep_s.sort()
            if  sort_prep_s == p_list:
                answer_list.append(i)


        return answer_list
        