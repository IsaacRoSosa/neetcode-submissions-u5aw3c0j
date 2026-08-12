class FreqStack:

    def __init__(self):
        self.counter = {}
        self.maxCnt = 0 
        self.stacks = {}

    def push(self, val: int) -> None:
        valCount = 1 + self.counter.get(val,0)
        self.counter[val] = valCount
        if valCount > self.maxCnt:
            self.maxCnt = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)
        
    def pop(self) -> int:
        val = self.stacks[self.maxCnt].pop()
        if not self.stacks[self.maxCnt]:
            self.maxCnt -=1
        self.counter[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()