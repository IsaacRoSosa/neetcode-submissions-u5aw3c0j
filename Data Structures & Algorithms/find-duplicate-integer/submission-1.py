class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #Find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #Start floids
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2
