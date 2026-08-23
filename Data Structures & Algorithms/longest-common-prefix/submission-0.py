class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return ans
            else:
                ans += strs[0][i]
        return ans



        