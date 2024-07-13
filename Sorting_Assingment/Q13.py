class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sum(1 for x in sorted_nums if x < num))
        return result