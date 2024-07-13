class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i, row in enumerate(mat):
            soldiers = row.count(1)
            rows.append((soldiers, i))
        rows.sort()
        return [x[1] for x in rows[:k]]
 