class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_list = []
        t_list = []
        
        for str in s:
            s_list.append(str)
        for str in t:
            t_list.append(str)
        
        s_list.sort()
        t_list.sort()

        if s_list == t_list:
            return True
        else:
            return False
