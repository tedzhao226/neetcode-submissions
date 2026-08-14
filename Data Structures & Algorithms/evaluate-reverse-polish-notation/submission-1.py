"""Evaluate Reverse Polish Notation (NeetCode 150 / LeetCode 150) - Medium.

PROBLEM
-------
Evaluate an arithmetic expression given in Reverse Polish Notation (postfix).
Tokens are integers or the operators +, -, *, /. Division truncates toward
zero. The expression is always valid, so the stack never underflows.

    ["2","1","+","3","*"]           ->  ((2 + 1) * 3) = 9
    ["4","13","5","/","+"]          ->  (4 + (13 / 5)) = 6
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]  ->  22


WHAT RPN IS
-----------
Infix writes the operator between operands and needs parentheses:

    (2 + 1) * 3

Postfix / RPN writes the operator AFTER its two operands. No parentheses:

    2 1 + 3 *

Read left to right. A number is a value. An operator means: take the two
values just produced, apply the operator, and that result is the new value.


WHY A STACK (LIFO), NOT A QUEUE (FIFO)
--------------------------------------
A stack is last-in, first-out. A queue is first-in, first-out. RPN needs
the stack, not the queue.

An operator always applies to the two MOST RECENT values, not the two oldest.
"Most recent" is the top of a stack.

Counter-example if we used a queue (FIFO) on ["4","13","5","/","+"]:

    queue: 4, 13, 5
    "/": dequeue 4 and 13  ->  4/13 = 0    WRONG
    the "/" was meant for 13 and 5, which arrived last

Stack (LIFO) does the right thing:

    stack: 4, 13, 5
    "/": pop 5 (right), pop 13 (left)  ->  13/5 = 2, stack = [4, 2]
    "+": pop 2, pop 4                  ->  4+2 = 6

That is also why we pop into `b` first, then `a`. The top is the right
operand. Subtraction and division are not commutative, so the order is the
whole problem:

    tokens ["5","2","-"]  ->  5 - 2 = 3, never 2 - 5


DIVISION
--------
LeetCode wants truncate-toward-zero, not Python floor division.

    int(7 / 2)   ==  3     int(-7 / 2)  == -3     toward zero
    7 // 2       ==  3     -7 // 2      == -4     toward -inf  (wrong here)

So we use int(a / b), not a // b. Operand order still matters: a is left.


WALKTHROUGH: ["2","1","+","3","*"]
----------------------------------
    token  stack (bottom -> top)     action
    -----  ------------------------  -----------------------------
    "2"    [2]                       number, push
    "1"    [2, 1]                    number, push
    "+"    pop b=1, pop a=2
           [3]                       2+1, push
    "3"    [3, 3]                    number, push
    "*"    pop b=3, pop a=3
           [9]                       3*3, push

The single remaining value is the answer.

O(n) time, O(n) space.
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,  # a is left: 5 2 -  =>  5-2, not 2-5
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # toward zero; a // b floors the wrong way
        }

        for t in tokens:
            if t in ops:
                # LIFO: top is the right operand. Pop b, then a.
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))

        return stack[0]
