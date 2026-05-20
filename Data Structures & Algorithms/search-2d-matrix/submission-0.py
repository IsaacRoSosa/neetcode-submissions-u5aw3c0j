class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arrays in matrix:
            for num in arrays:
                if num == target:
                    return True
            
        return False