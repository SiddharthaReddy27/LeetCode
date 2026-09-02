class Solution(object):
    def findMaxAverage(self, nums, k):
    

        window_sum = sum(nums[:k])
        max_sum = window_sum

        left = 0

        for right in range(k, len(nums)):
            window_sum -= nums[left]
            left += 1
            window_sum += nums[right]

            max_sum = max(max_sum, window_sum)

        return max_sum /float(k) 
        