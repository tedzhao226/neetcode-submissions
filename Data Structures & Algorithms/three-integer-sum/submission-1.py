class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # turn the question in to find items[j] + item[k] = target
        # sort it
        # deduplicating
        # apply the two items
        # while loop
        # also need to deal with duplication

        res = []
        nums.sort()

        # conern case
        if nums[0] > 0:
            return []

        # why len(nums) - 2
        for i in range(len(nums) - 2):
            # deduplicated
            if i > 0 and (nums[i - 1] == nums[i]):
                continue

            j, k = i + 1, len(nums) - 1

            # i + j + k = 0
            # j + k = -i

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                elif total == 0:  # found triplet
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    raise

        return res
