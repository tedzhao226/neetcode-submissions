class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # step 1
        # counts freq

        # step 2
        # sorting the buckets which is really expensive op

        # the key is that turn the sorting into a keymap

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # why + 1, bc if all the same will need the extra position to make up for the starting point
        # is 0
        # buckets of different freq...
        # this line causing shadow reference...
        # buckets = [[]] * (len(nums) + 1)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        top_k = []

        # why minus 1 here ?
        # ok.. bc index in last is n - 1
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
            
                
        