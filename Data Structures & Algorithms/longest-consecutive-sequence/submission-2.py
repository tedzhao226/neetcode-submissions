class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # find the start of seq, then find the longest seq

        if not nums:
            return 0

        h_num = set(nums)
        start_nums = []

        for num in nums:
            
            if (num - 1) not in h_num:
                start_nums.append(num)
                
        seq_max = -float("inf")

        for s in start_nums:
            seq = [s]

            while (s + 1) in h_num:
                seq.append(s + 1)
                s += 1
            
            seq_max = max(len(seq), seq_max)
        
        return seq_max
                
            
            

            
            