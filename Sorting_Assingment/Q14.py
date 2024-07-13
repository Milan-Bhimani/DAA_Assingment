sclass Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        nums.sort(key=lambda x: (count[x], -x))
        return nums