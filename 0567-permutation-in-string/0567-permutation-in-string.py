class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list, s2_list = sorted(list(s1)), list(s2)

        for i in range(len(s2) - len(s1) +1):
            s2_sclicing_list = sorted(s2_list[i:i+len(s1)])

            if  s2_sclicing_list == s1_list:
                return True
        
        return False
            
