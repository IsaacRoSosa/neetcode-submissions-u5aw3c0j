# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def qSort(arr, s, e):
            #base case arr size 1
            if e-s+1 <=1:
                return arr

            pivot = arr[e]
            left = s

            for i in range(s,e):
                if arr[i].key < pivot.key:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    left +=1
            
            arr[e] = arr[left]
            arr[left] = pivot

            qSort(arr, s, left-1)
            qSort(arr, left+1, e)

            return arr
        qSort(pairs,0, len(pairs)-1)
        return pairs        