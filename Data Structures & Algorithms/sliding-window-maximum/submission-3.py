from collections import deque

"""
===============================================================================
 239. SLIDING WINDOW MAXIMUM  —  max of every k-sized window.
 Solution: MONOTONIC DEQUE.  O(n) time, O(k) space.
===============================================================================

WHAT THE PROBLEM ACTUALLY ASKS FOR
    Not "a trick". It asks you to implement a MAX-QUEUE: a FIFO queue with
        push_back(x)      pop_front()      max()
    The core difficulty is a state recorder for the window that survives BOTH
    mutations — one element enters right, one leaves left — without recomputing
    max() in O(k). The monotonic deque is one implementation; the max-queue is
    the idea.

THE KEY INSIGHT — DOMINANCE
    Every element has TWO attributes: its VALUE and its EXPIRY TIME (= index).

        Element i is USELESS FOREVER if some j > i has nums[j] >= nums[i],
        because j is both BIGGER and OUTLIVES i.

    There is no future window where i is the answer and j is absent. So i is
    *dominated* and can be discarded the instant j arrives. Keep only the
    non-dominated elements and the deque holds exactly the candidate set.

THE TWO ORDERINGS  (the part that is easy to get backwards)
    The deque carries two sorted orders at once, running OPPOSITE ways:

        FRONT ───────────── position in deque ─────────────► BACK
  age:  oldest                                               newest
value:  largest                                              smallest
        ^^^^^^^^^^^^^^^^                                     ^^^^^^^^
        strongest on both                                 weakest on both

    Why they are FORCED to run opposite: the window expires FIFO — the left
    edge only ever moves right — so "older" and "dies sooner" are the same
    thing. An element earns its place only by beating everyone YOUNGER than
    it. An old small element beside a young big one is pointless: the young
    one is better now AND lasts longer. That is what welds the orders together.
    Break FIFO expiry and the alignment collapses — that is when you need a heap.

MNEMONIC — THE LINE OF SUCCESSION
        dq[0] = the reigning champion (current window max)
        dq[1] = the heir: the best element YOUNGER than the champion,
                waiting for the champion to expire
        dq[2] = the heir's heir ... and so on
    Each successor is necessarily younger AND weaker — younger because it
    arrived later, weaker because if it were stronger it would have deposed
    the one ahead of it on arrival. Hence DECREASING, not increasing.

        a new arrival kills every pretender it outranks  -> the while loop
        then joins the back of the line                  -> append
        when the king dies of old age                    -> popleft
        the heir is already standing there               -> answer is O(1)

INVARIANT — true at the top of every iteration
        1. indices in dq INCREASE         front = oldest, back = newest
        2. nums[dq] is NON-INCREASING     front = largest
        3. every index in dq is in the current window
        => dq[0] is always the answer. No scanning. The structure IS the answer.

    `nums[dq]` is shorthand, not real Python — "the values at the indices in
    dq, front to back":
            dq       = [ 1,  4,  6 ]     <- indices  (increasing)
            nums[dq] = [ 9,  5,  2 ]     <- values   (non-increasing)

    NON-increasing, not strictly decreasing: the loop pops only on `<`, so
    equal values survive side by side (nums=[3,3] -> nums[dq]=[3,3]). Still
    correct — the front duplicate expires first and hands the answer to the
    identical one behind it. `<=` would make it strict and keep the deque
    shorter, at the cost of pop/push churn on runs of duplicates. Both O(n).

WHY O(n)
    Each index is appended exactly once and popped at most once, so the inner
    while-loop performs <= n pops in TOTAL. Amortized O(1) per element, even
    though a single step may pop many — see right=4 below, where one big
    element wipes the whole deque.

TRACE   nums = [1, 2, 1, 0, 4, 2, 6], k = 3
        right=0  num=1                  dq=[0]        vals (1)
        right=1  num=2   1<2, pop idx0  dq=[1]        vals (2)       -> out 2
        right=2  num=1                  dq=[1,2]      vals (2,1)     -> out 2
        right=3  num=0                  dq=[1,2,3]    vals (2,1,0)   -> out 2
        right=4  num=4   pop 3,2,1      dq=[4]        vals (4)       -> out 4
        right=5  num=2                  dq=[4,5]      vals (4,2)     -> out 4
        right=6  num=6   pop 5,4        dq=[6]        vals (6)       -> out 6
    (at right=3 the king idx1 is still alive: 3 - 1 = 2 < k. It is not
     expired — it gets deposed at right=4 instead.)

TERMINOLOGY  (so you can look this up later)
    Monotonic deque / monotonic queue   this structure. Sibling: monotonic
                                        STACK, for next-greater-element.
    Dominance pruning                   the discard rule above.
    Pareto frontier / skyline /         formal name for "non-dominated set
      staircase / maximal set           under two criteria". The deque IS a
                                        Pareto frontier over (value, expiry).
    Suffix maxima                       what that frontier equals concretely.
    Monotonic queue optimization        the name when used to speed up DP.

HONOURABLE MENTIONS  (same ADT, different implementations — know they exist)
    1. MAX-HEAP WITH LAZY DELETION — O(n log n) time, O(n) space.
       Push (-num, idx); the expiring element sits at an ARBITRARY position so
       it cannot be removed cheaply — leave the garbage in and pop stale tops
       only when they surface. Slower and the heap can grow to O(n) despite a
       window of k, BUT it is the general solution: it never discards, so it
       still knows the 2nd/3rd largest, and it survives NON-FIFO expiry, where
       the dominance argument is invalid.
    2. TWO MAX-STACKS — O(n) amortized.
       A stack tracks its own running max trivially (push the pair
       (x, max(x, max_so_far))); a queue is two stacks; therefore a max-queue
       is two max-stacks and max() = max of the two tops. Proof that the deque
       is not the essence of the answer — the MAX-QUEUE ADT is.

IS THE DEQUE JUST A DIFFERENT KIND OF HEAP?
    Tempting — a sorted sequence IS heap-ordered, so the deque reads as a heap
    whose tree is a single path, and the pop-while loop rhymes with sift-up.
    But two things a heap never does:
        1. IT DISCARDS. A heap is a faithful multiset of the window; the deque
           is a lossy filter. Popping a live element that is not the extremum
           is not a heap operation at all.
        2. IT IS DOUBLE-ENDED. Max leaves at the front (expiry), losers leave
           at the back (dominance).
    Sanity check: no general priority queue can have O(1) insert AND O(1)
    delete-max, or you would have an O(n) comparison sort. The deque does not
    violate that bound — it escapes it by refusing to remember everything.
        heap  = a faithful container that happens to expose a max
        deque = a max-oracle that happens to be stored in order
===============================================================================
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # dq holds INDICES, never values — indices are what detect expiry.
        dq: deque[int] = deque()
        out: list[int] = []

        for right, num in enumerate(nums):

            # (a) EVICT THE DOMINATED — restores invariant 2.
            #     Anything smaller than `num` is also OLDER: smaller AND
            #     expires first => dead forever. This discard IS the algorithm.
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # (b) The newcomer is always a candidate — nothing outlives it yet.
            dq.append(right)

            # (c) EVICT THE EXPIRED — restores invariant 3.
            #     Window is [right-k+1, right] => index i is dead iff
            #     right - i >= k. Only the FRONT can expire (indices increase),
            #     at most one per step => `if`, not `while`.
            if right - dq[0] >= k:
                dq.popleft()

            # (d) The first full window ends at index k-1.
            if right >= k - 1:
                out.append(nums[dq[0]])

        return out