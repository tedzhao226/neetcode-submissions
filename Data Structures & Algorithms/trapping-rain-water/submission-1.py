class Solution:
    def trap(self, height: List[int]) -> int:
        """
        two points

        it is really hard to understand, it took me 1 hour now, fuck

        the tricky part is the current trap water representation 

        w[i] = min(height[l], height[r]) - height[i]

        in two point, it uses height[l] < height[r] to figure out the min part.

        overall, it is harder to follow through the idea compare to the prefix / suffix method

        the way in two point how it does, is still monotonically iterate one elemnent a time, 

        so it certainly accompanies with a if with the while true

        """

        l, r = 0, len(height) - 1
        l_max , r_max = height[l], height[r]
        total = 0

        while l < r:

            if height[l] < height[r]:

                l += 1
                l_max = max(l_max, height[l])
                total += l_max - height[l]
            
            else:
                r -= 1
                r_max = max(r_max, height[r])
                total += r_max - height[r]

        return total
            
