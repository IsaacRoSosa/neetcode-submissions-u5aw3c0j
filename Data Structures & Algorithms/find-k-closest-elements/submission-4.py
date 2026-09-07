class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k

        while l < r:
            m = (l+r)//2
            ws = arr[m] #Window Start / a
            nWE = arr[m+k]#next window end / b
            #Assuming x is greather than ws
            if x - ws > nWE-x:
                l = m+1 #adjust window to the right
            else:   #The
                r = m
        return arr[l:l+k]