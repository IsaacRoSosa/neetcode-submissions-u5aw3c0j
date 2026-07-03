class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        l,r = 0, len(values) - 1 
        ans = ""

        while l<=r:
            m = (l+r) // 2
            #Si es menor 
            if values[m][1] <= timestamp:
                #Buscar si hay uno mayor ->
                ans = values[m][0]
                l = m+1
            else:
                r = m-1
        return ans

        
