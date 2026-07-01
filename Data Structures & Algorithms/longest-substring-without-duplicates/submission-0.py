class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l,r = 0,0

        while r < len(s):
            #Move L pointer N spots
            if s[r] in seen:
                n = seen[s[r]]
                while l <= n:
                    del seen[s[l]]
                    l+=1
            #asiganr index al diccionario
            seen[s[r]] = r

            size = r-l + 1
            ans = max(ans, size)

            r += 1
        return ans