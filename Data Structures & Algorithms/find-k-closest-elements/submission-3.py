class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = arr[:k]
        score = float("inf")
        for i in range(k-1, len(arr)):
            window = arr[i-k+1:i+1]
            curScore = sum(abs(num - x) for num in window)

            if curScore < score:
                score = curScore
                ans = window

        return ans