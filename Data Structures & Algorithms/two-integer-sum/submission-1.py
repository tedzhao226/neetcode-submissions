class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        matches = {}

        for j, num in enumerate(nums):
            res = target - num

            if res in matches:
                i = matches.get(res)
                return [i, j]
            else:
                matches[num] = j                

