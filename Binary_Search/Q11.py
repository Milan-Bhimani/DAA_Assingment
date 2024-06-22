class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                candidate = letters[mid]
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1
            else:
                return letters[mid]
        if target < letters[0]:
            return letters[0]  
        else:
            return letters[1] if len(letters) > 1 else target