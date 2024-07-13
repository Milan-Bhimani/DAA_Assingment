class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        even = sorted([nums[i] for i in range(0, len(nums), 2)])
        result = []
        for i in range(len(even)):
            result.append(even[i])
            if i < len(odd):
                result.append(odd[i])
        return result