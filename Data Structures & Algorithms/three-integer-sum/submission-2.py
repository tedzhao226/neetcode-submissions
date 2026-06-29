class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort

        1 - turn it into the 2sum, by fixing the first element, using i j k

        2 - for loop first i, apply 2 sum for the rest

        2.1 - loop need to check the duplicate for i

        3 - while loop

        3.1 check duplication for j / k
        3.2 we use the monotic function again if total < 0 , j += 1, if total > 0 k -= 1

        """

        res = []
        nums.sort()

        for i in range(len(nums) - 2):

            # skip duplication
            if (i > 0) and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:  # find the triplets
                    res.append([nums[i], nums[j], nums[k]])

                    # move to next round
                    j += 1
                    k -= 1

                    # deal with duplications in j, k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res
