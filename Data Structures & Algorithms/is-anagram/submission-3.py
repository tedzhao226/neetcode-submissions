class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        for j in t:
            if j in counts:
                counts[j] -= 1
            else:
                return False
        
        return all([x == 0 for x in counts.values()])