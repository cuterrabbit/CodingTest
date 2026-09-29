class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if 0 not in nums:
            return 0
        nums.sort()
        nums_table={
        }
        for num in nums:
            nums_table[num]=True
        for num in nums:
            if num+1 in nums_table:
                pass
            else:
                return num+1