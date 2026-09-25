class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):

            if i == len(nums):
                break

            for j in range(i +1, len(nums)) :
                
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        return False


    def twoSum1(self, nums: list[int], target: int) -> list[int]:

        if len(nums) == 2:
            return [0,1]
        
        dict_nums={}
        for i,n in enumerate(nums):
            if n not in dict_nums.keys():
                dict_nums[n] = []
            dict_nums[n].append(i)
        
        for num in dict_nums.keys():
            need = target - num
            if need in dict_nums.keys():
                if need == num and len(dict_nums[num]) >= 2:
                    return[int(dict_nums[num][0]),
                     int(dict_nums[num][1])
                     ]
                
                elif need != num:
                    return [dict_nums[num][0], dict_nums[need][0]]
