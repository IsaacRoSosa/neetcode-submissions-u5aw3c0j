class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        while l < len(height):

            if height[l]:
                cur = 0
                r = l + 1
                found_equal_or_higher = False
                while r < len(height) and not found_equal_or_higher:
                    if height[r] >= height[l]:
                        water += cur
                        l = r - 1
                        found_equal_or_higher = True
                    else:
                        cur += height[l] - height[r]
                    r += 1
        
                if not found_equal_or_higher and l < len(height) - 1:
                    max_right_val = -1
                    max_right_idx = -1

                    for i in range(l + 1, len(height)):
                        if height[i] > max_right_val:
                            max_right_val = height[i]
                            max_right_idx = i
                    if max_right_idx != -1:
                        for i in range(l + 1, max_right_idx):
                            water += max_right_val - height[i]
                        l = max_right_idx - 1
            l += 1 
        return water