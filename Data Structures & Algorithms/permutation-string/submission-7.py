class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def alphebet_to_index(letter: str) -> int:
            if len(letter) > 1 :
                raise ValueError()
            return ord(letter) - ord("a")

        # corner case if the len of s1 is greater than s2 return false
        if len(s1) > len(s2):
            return False

        # sliding windows 
        left = 0
        letters_counts_map = [0] * 26
        s1_map = [0] * 26
        window_size = len(s1)

        for i in s1:
            s1_map[alphebet_to_index(i)] += 1

        for right in range(len(s2)):
            
            if (right - left + 1) <= window_size:
                letters_counts_map[alphebet_to_index(s2[right])] += 1
            else:
                letters_counts_map[alphebet_to_index(s2[left])] -= 1
                left += 1
                letters_counts_map[alphebet_to_index(s2[right])] += 1

            if letters_counts_map == s1_map:
                return True

        return False
        

        