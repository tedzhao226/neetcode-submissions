class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the key is to figure the condition when to shrink the window


        def letter_to_int(letter: s):
            return ord(letter) - ord("A")


        left = 0
        feq_map = [0] * 26
        max_freq = 0
        longest = 0

        for right in range(len(s)):

            feq_map[letter_to_int(s[right])] += 1
            max_freq = max(max_freq, feq_map[letter_to_int(s[right])])

            num_replacable = right - left + 1 - max_freq

            if num_replacable > k:
                feq_map[letter_to_int(s[left])] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest
        