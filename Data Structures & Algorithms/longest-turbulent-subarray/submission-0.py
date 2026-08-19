class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l +1)
                r+=1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l +1)
                r+=1
                prev = "<"
            #Equal
            else:
                if arr[r] == arr[r-1]:
                    r = r+1
                l = r - 1
                prev = ""
        return res




        