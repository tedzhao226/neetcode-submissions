class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # two pointers
        # find mononic, it will guide which pointer to move, only move the pointer to the position leader a mononic direction 
        # towards you better result ( min / max)

        l, r = 0, len(heights) - 1
        s_max = 0

        while l < r:

            s = min(heights[l], heights[r]) * (r - l)
            s_max = max(s, s_max)

            if heights[l] < heights[r]:
                # l is the smaller one, so I want to replace it, since (r - l) is shrinking, only when we swap the smaller barrier
                # leads to larger total water
                l += 1
            else:
                r -= 1

        return s_max