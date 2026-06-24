class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        
        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)            

    def decode(self, s: str) -> List[str]:

        # i need to understand the two points 

        i = 0

        decoded_strs = []

        while i < len(s):

            """
            - find the j poistion ( when # is )
            - find the length
            - move i to the start of the actual content
            - extract content
            - move i forward to process new segment
            """
            j = i
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            content = s[i:i + length]
            decoded_strs.append(content)
            i += length
        
        return decoded_strs
