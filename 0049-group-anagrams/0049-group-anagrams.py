class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output=[]
        dict_anagrams={}
        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in dict_anagrams:
                dict_anagrams[s_sort]=[]
            dict_anagrams[s_sort].append(s)
        for s in dict_anagrams.keys():
            output.append(dict_anagrams[s])
        return output