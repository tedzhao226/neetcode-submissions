class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def idx(letter: str) -> int:
            return ord(letter) - ord("a")

        window_size = len(s1)
        s1_map = [0] * 26
        window_map = [0] * 26

        # build frequency count for s1
        for c in s1:
            s1_map[idx(c)] += 1

        # slide a fixed-size window over s2
        for right in range(len(s2)):
            window_map[idx(s2[right])] += 1

            # once the window exceeds size, drop the char that fell out
            if right >= window_size:
                window_map[idx(s2[right - window_size])] -= 1

            if window_map == s1_map:
                return True

        return False