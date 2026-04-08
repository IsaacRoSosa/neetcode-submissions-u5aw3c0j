class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                #tenemos que cambiar el valor en nuestra solution
                stackI, stackT = stack.pop()
                solution[stackI] = (i - stackI)

            stack.append([i,t])
        return solution
        
