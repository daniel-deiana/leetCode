"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""



class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def robHouse(i):
            if i >= len(nums):
                return 0
            

            if i not in cache:
                robCurrent = nums[i] + robHouse(i+2)
                robNext = robHouse(i+1)
                cache[i] = (robCurrent,robNext)
            else:
                robCurrent = cache[i][0]
                robNext = cache[i][1]
                
            return max(robCurrent,robNext)
        
        return robHouse(0)
