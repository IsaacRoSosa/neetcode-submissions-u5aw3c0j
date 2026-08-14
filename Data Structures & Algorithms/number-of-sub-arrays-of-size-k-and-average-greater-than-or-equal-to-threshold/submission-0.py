class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0 
        wTotal = 0
        L = 0

        for R in range(len(arr)):
            wTotal += arr[R]
            #Window size is less then k
            if R - L + 1 > k:
                wTotal -= arr[L]
                L += 1
            if R - L + 1 == k:
                if wTotal >= threshold * k:
                    ans +=1
        return ans

            