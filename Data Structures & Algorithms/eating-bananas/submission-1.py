class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:

            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            #si nos falto, moverse a la derecha
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k-1
                ans = min(ans,k)
        return ans



        