class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # GIST:
        # We want to know if any substring of s2 is a permutation (anagram)
        # of s1. A permutation has the exact same character counts, so we
        # slide a FIXED-size window (size = len(s1)) across s2 and keep a
        # running frequency count of the window. Whenever the window's
        # counts match s1's counts, we've found a permutation.
        #
        # Since the window size never changes, we don't need a separate
        # `left` pointer: the character leaving the window is always the
        # one `window_size` positions behind the current index.

        if len(s1) > len(s2):
            return False

        def idx(letter: str) -> int:
            return ord(letter) - ord("a")

        window_size = len(s1)
        s1_map = [0] * 26      # target character counts (from s1)
        window_map = [0] * 26  # character counts in the current window

        # build the target frequency count for s1
        for c in s1:
            s1_map[idx(c)] += 1

        # slide a fixed-size window across s2
        for right in range(len(s2)):
            window_map[idx(s2[right])] += 1

            # once the window exceeds its size, drop the char that fell out
            if right >= window_size:
                window_map[idx(s2[right - window_size])] -= 1

            if window_map == s1_map:
                return True

        return False