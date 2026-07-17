class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # GIST:
        # Use a sliding window. A window is "valid" if we can make every
        # character in it the same by replacing at most k characters.
        # The number of replacements needed = (window size) - (count of the
        # most frequent character in the window). If that exceeds k, the
        # window is too big, so we slide the left edge forward by one.
        #
        # Key trick: we never decrease max_freq when shrinking. A smaller
        # max_freq could only produce a smaller window, and we only care
        # about the LONGEST window ever found — so letting max_freq stay
        # "stale" is safe and keeps the whole thing O(n).

        def letter_to_int(letter: str) -> int:
            return ord(letter) - ord("A")

        left = 0
        freq_map = [0] * 26   # frequency of each letter in the current window
        max_freq = 0          # highest single-letter count seen in any window
        longest = 0

        for right in range(len(s)):
            freq_map[letter_to_int(s[right])] += 1
            max_freq = max(max_freq, freq_map[letter_to_int(s[right])])

            # chars we'd need to replace to make the window uniform
            num_replaceable = (right - left + 1) - max_freq
            if num_replaceable > k:
                # window too big: drop the leftmost char and advance
                freq_map[letter_to_int(s[left])] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest