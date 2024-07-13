class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                duplicates.append(num)
            else:
                nums[num - 1] *= -1
        return duplicates