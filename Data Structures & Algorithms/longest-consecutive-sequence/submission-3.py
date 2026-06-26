class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # find the start of seq, then find the longest seq
        h_num = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in h_num:

                start_num = num
                length = 1

                while (start_num + 1) in h_num:
                    start_num += 1
                    length += 1

                longest = max(length, longest)
        
        return longest

            
            