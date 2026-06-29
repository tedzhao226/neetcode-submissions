class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two points before the non-decreating series 
        # we can ustilise the nums[0] + nums[n-1] > target, to narrow down the answer (it is basically like a search ...?)
        # I can relate that to the monotonic function(right?)

        
        # return 1 indexed

        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -=1 

                
        