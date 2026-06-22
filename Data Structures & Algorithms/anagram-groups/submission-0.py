class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # enumerate each word, and encode it

        groups = {}

        for word in strs:
            encoded = [0] * 26

            for char in word:
                i = ord(char) - ord("a")
                encoded[i] += 1

            encoded: tuple = tuple(encoded)

            if encoded in groups:
                item = groups[encoded]
                item.append(word)
                groups[encoded] = item
            else:
                groups[encoded] = [word]

        return list(groups.values())