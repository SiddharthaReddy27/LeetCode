class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for i in range(len(nums)):
            n=target-nums[i]

            if n in seen:
                return seen[n],i

            seen[nums[i]] = i
         
        
        