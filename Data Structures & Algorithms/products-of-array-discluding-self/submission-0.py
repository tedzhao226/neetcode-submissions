class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # first pass 
        # left to right, starting from 1 - n
        # ans[i] = nums[i-1] * ans[i-1]

        n = len(nums)
        prefix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # second pass
        running_prod = 1
        for i in range(n-1, -1, -1):
            prefix[i] *= running_prod
            running_prod *= nums[i]

        return prefix
