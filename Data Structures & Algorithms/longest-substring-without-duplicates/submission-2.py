class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l=0

        for r in range(len(s)):
            #Move L pointer N spots
            if s[r] in seen:
                l = max( seen[s[r]] + 1,l)
            #asiganr index al diccionario
            seen[s[r]] = r
            ans = max(ans, r-l + 1)
        return ans