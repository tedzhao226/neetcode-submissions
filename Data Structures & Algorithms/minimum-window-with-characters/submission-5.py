from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Shortest substring of `s` holding every char of `t`, duplicates included.

        Validity is monotone: if a window is valid, so is every window containing
        it. So `left` never moves backwards. Both pointers only advance, each
        index enters and leaves once, and the scan is O(n).

        Loop invariant, restored on every iteration:

            have == |{ c in need : window[c] >= need[c] }|
            window is valid  <=>  have == required
        """
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)  # distinct chars to satisfy, not len(t)

        window: dict[str, int] = {}
        have = 0  # how many of those are satisfied right now

        # Hold the answer as (start, length). Slicing inside the loop would turn
        # an O(n) scan into O(n^2).
        best_len = float("inf")
        best_left = 0

        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            # `==`, not `>=`. A char may exceed its quota, but it crosses the
            # threshold once, so it earns exactly one credit.
            if char in need and window[char] == need[char]:
                have += 1

            # Valid. Pull `left` in as far as validity survives.
            while have == required:
                # Record here, before dropping: the window is still valid.
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                dropped = s[left]
                window[dropped] -= 1

                # `<`, not `<=`. Mirror of the add rule. `<=` gives up the credit
                # while the quota is still met, exits the loop one step early,
                # and returns a window that is too long.
                if dropped in need and window[dropped] < need[dropped]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_left : best_left + best_len]
