"""
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def partition(i,a,b):          
            if i > len(nums):
                return False

            # either make the choice to include the current
            # element in the first or second subset
            if i == len(nums):
                return a == b

            return partition(i+1, a + nums[i], b) | partition(i+1,a, b+nums[i])

        return partition(0,0,0)
