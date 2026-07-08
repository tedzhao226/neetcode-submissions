class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # a seen set to check the have seen charactor
        # l, r: loop through r 
        # windows slice, if we have seen the new charactor from r, 
        # if we have seen it, we need to shirnk the window, and remove the duplication 

        seen = set()
        l = 0
        length = 0

        for r in range(0, len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            length = max(length, r - l + 1)

        return length
