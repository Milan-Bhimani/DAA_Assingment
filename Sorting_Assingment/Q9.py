class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]
        sorted_score = sorted(score, reverse=True)
        return [rank[sorted_score.index(i)] for i in score]