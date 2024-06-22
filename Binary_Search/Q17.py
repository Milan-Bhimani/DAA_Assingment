class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0    
        expected = 1
        for num in arr:
            while num > expected:
                missing_count += 1
                if missing_count == k:
                    return expected
                expected += 1
            expected += 1
        return arr[-1] + k - missing_count