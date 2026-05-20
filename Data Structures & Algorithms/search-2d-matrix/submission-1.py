class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = l + ((r-l) //2)
                #Si es mayor
                if arr[m] > target:
                    r = m-1
                #Si el numero es menor
                elif arr[m] < target:
                    l = m+1
                else:
                    return True
            return False

        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + ((r-l) //2)
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                return binarySearch(matrix[m])
            elif matrix[m][-1] < target:
                l = m + 1
            #Si el numero es menor
            elif matrix[m][0] > target:
                r = m - 1
        return False
