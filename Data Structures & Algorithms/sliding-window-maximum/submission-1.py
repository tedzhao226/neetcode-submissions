from collections import deque

"""
1 - use Monotonic dq to store the window
2 - 
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq: deque[int] = deque() # for the indices, value is decreasing only ( from right to left)
        out: list[int] = []

        for right, num in enumerate(nums):
            
            # keep dq Monotonic 
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(right)

            # pop out, ele out of windows

            if right - dq[0] >= k:
                dq.popleft()

            if right >= k - 1:
                out.append(nums[dq[0]])
        
        return out
