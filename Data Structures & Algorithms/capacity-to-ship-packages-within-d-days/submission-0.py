class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r
        while l <= r:
            maxCap = (l+r) // 2
            d = 0
            curr = 0
            for package in weights:
                if curr + package > maxCap:
                    curr = package
                    d +=1
                else:
                    curr += package
            if curr:
                d += 1

            if d <= days:
                r = maxCap-1
                ans = min(ans, maxCap)
            else:
                l = maxCap+1
        return ans