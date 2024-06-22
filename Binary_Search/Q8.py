class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                end = mid
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

