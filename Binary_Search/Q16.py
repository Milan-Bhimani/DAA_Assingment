class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low = max(nums) 
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            subarray_sum = 0
            subarrays = 1
            can_split = True
            for num in nums:
                subarray_sum += num
                if subarray_sum > mid:
                    subarrays += 1 
                    subarray_sum = num 
                    if subarrays > k:
                        can_split = False
                        break
            if can_split:
                high = mid - 1
            else:
                low = mid + 1
        return low