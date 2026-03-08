
"""
You are given an integer n representing the number of steps to reach the top of a staircase. 

You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

    Input: n = 2

    Output: 2

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def step(pos):
            if pos > n:
                return 0
            elif pos == n:
                return 1
                
            if pos not in cache:
                comb = step(pos+1) + step(pos+2)
                cache[pos] = comb
            else:
                comb = cache[pos]
            return comb
        return step(0)

