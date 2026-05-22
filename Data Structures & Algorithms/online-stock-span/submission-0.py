class StockSpanner:

    def __init__(self):
        self.decreaseStack = []


    def next(self, price: int) -> int:
        val = 1
        while self.decreaseStack and price >= self.decreaseStack[-1][0]:
            num, cost = self.decreaseStack.pop()
            val += cost
        self.decreaseStack.append((price,val))

        return(val)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)