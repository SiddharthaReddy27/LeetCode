class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
           

        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= threshold * k:
            count += 1

        left = 0

        for right in range(k, len(arr)):

            window_sum -= arr[left]
            left += 1
            window_sum += arr[right]

            if window_sum >= threshold * k:
                count += 1

        return count

        