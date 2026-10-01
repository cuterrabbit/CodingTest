class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first, second = strs[0], strs[-1]
        min_length = min(len(first), len(second))
        n = 0
        for i in range(min_length):
            if first[i] == second[i]:
                n += 1
            else:
                break
        if n == 0:
            return ""
        return first[0:n]