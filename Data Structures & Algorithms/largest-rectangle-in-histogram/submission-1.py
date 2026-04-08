class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (i,h)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                  index, heigth = stack.pop()
                  maxArea = max(maxArea, heigth * (i - index))
                  start = index
            stack.append([start,h])
        #Los que se pudieron quedar hasta el final
        for i,h in (stack):
            maxArea = max(maxArea , (h * (len(heights)-i)))
        return maxArea



        return maxArea


        
