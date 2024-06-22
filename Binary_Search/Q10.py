class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        assert x > 0, "Input must be a non-negative integer"
        result = int(x ** 0.5)  
        end = x // 2  
        while result * result > x and result <= end:
            result = (result + end) // 2
        return result