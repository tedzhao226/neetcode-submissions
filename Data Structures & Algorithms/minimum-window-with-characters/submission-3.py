from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        the window slice, left
        condition

        - valid: the window having the same unique letters as the substring
        - map(target) = map(windows)
        - having len(widows) min


        grow if the not valid
        shrink, when we have a valid right


        THE KEY OBSERVATION
        -------------------
        Validity is monotone. If a window is valid, every window that contains it is
        also valid. So for each right end, there is exactly one leftmost `left` that
        still keeps the window valid. Push `left` one step further and the window
        breaks.
        """

        # corner case
        if not s or not t:
            return ""

        # target
        need: dict[str, int] = Counter(t)
        required: int = len(need)

        window: dict[str, int] = {}
        have: int = 0

        best_len = float("inf")
        best_left = 0

        left = 0
        for right, char in enumerate(s):
            # checking the fucking char            
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1
            
            # shrink
            while have == required:

                # check the best outcome
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                
                # drop and shrink
                dropped = s[left]
                window[dropped] -= 1

                # update the status of windows
                if dropped in need and window[dropped] < need[dropped]:
                    have -= 1
                left += 1
        
        if best_len == float("inf"):
            return ""
        return s[best_left: best_left + best_len]

            




