
"""
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. 
After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def step(i):
            if i >= len(cost):
                return 0
            
            if i not in cache:
                minPay = cost[i] + min(step(i+1), step(i+2))
                cache[i] = minPay
            else:
                minPay = cache[i]

            return minPay
