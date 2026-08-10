from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # dq holds INDICES, never values (indices are what detect expiry).
        #
        # INVARIANT, true at the top of every iteration:
        #   1. indices increase        (front = oldest, back = newest)
        #   2. nums[dq] strictly DECREASES  (front = largest)
        #   3. every index is inside the window
        # => dq[0] is always the current answer.
        dq: deque[int] = deque()
        out: list[int] = []

        for right, num in enumerate(nums):

            # (a) EVICT THE DOMINATED — restores invariant 2.
            # Anything smaller than `num` is also OLDER than it: smaller AND
            # expires first => dead forever. This discard is the whole trick.
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # (b) The newcomer is always a candidate — nothing outlives it yet.
            dq.append(right)

            # (c) EVICT THE EXPIRED — restores invariant 3.
            # Window is [right-k+1, right], so index i is dead iff right-i >= k.
            # Only the FRONT can expire, and at most one per step => `if`, not `while`.
            if right - dq[0] >= k:
                dq.popleft()

            # (d) First full window ends at index k-1.
            if right >= k - 1:
                out.append(nums[dq[0]])

        return out

        # O(n): each index is appended once and popped at most once, so the
        # inner while does <= n pops in TOTAL. Amortized O(1), even though a
        # single step can pop many.