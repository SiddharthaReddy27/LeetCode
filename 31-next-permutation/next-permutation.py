class Solution(object):
    def nextPermutation(self,nums):

    # Step 1: Find the pivot
        pivot = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

    # Step 2: If no pivot exists, reverse the entire array
        if pivot == -1:
            nums.reverse()
            return

    # Step 3: Find the smallest element greater than the pivot
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

    # Step 4: Reverse the elements after the pivot
        left = pivot + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        