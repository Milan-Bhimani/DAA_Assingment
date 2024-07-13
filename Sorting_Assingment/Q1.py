class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
            # Swap nums[low] and nums[mid], increment both low and mid pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
            # No swap needed, just move mid pointer forward
                mid += 1
            else:  # nums[mid] == 2
            # Swap nums[mid] and nums[high], decrement high pointer
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
