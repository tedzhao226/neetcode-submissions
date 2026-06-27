class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # normalisation
        s_n = "".join([i.lower() for i in s if (i.isdigit() or i.isalpha())])

        print(s_n)

        # two point algo
        p1 = 0
        p2 = len(s_n) - 1


        while p1 < p2:
            if s_n[p1] != s_n[p2]:
                return False

            p1 += 1
            p2 -= 1

        return True