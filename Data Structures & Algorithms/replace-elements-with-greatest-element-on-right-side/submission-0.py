class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        largest = arr[-1]

        while n > -1:
            if arr[n] >= largest:
                temp =  arr[n]
                arr[n] = largest
                largest = temp
            else:
                arr[n] = largest
            print(arr[n])
            n -= 1

        arr[-1] = -1
        
        return arr