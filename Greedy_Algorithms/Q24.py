class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones = [1] * numOnes
        zeros = [0] * numZeros
        neg_ones = [-1] * numNegOnes
        items = ones + zeros + neg_ones
        items.sort(reverse=True)
        return sum(items[:k])