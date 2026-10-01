class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = 0
        last_idx = 0
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                sum += nums[i]
                last_idx = i + 1
            else:
                break
        
        if last_idx == 0:
            sum = nums[0]
        else:
            sum += nums[last_idx]
            
        while True:
            if sum in nums:
                sum += 1
            else:
                return sum