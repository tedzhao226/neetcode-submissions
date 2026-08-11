"""Min Stack (NeetCode 150 / LeetCode 155) - Medium.

PROBLEM
-------
Support push, pop, top, and getMin, each in O(1).

THE HINT
--------
getMin is the only hard part. A single `self.min` variable breaks on pop: after
popping the minimum you cannot recover the previous one.

So store the minimum WITH each element. Every entry carries the minimum of the
stack as it looked when that entry was pushed. Pop removes the value and its
minimum together, and the entry below already holds the correct answer.

    push 3  ->  [(3,3)]
    push 5  ->  [(3,3), (5,3)]
    push 1  ->  [(3,3), (5,3), (1,1)]
    pop     ->  [(3,3), (5,3)]        getMin is 3 again, no recompute

O(1) for all four operations, O(n) space.
"""


class MinStack:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []  # (value, min at this depth)

    def push(self, val: int) -> None:
        # The new minimum is either val or the minimum already on top.
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        # Dropping the pair restores the previous minimum for free.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
