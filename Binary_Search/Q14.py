class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if n == 1:
            return 0 if nums[0] == target else -1

        if n == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, n - 1
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1