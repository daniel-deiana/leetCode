def generateSubsets(nums: list, i: int, curr: list):

    if i >= len(nums):
        return [curr]

    # generate the set that has the current element and the one that hasn't
    has = curr + [nums[i]]

    return generateSubsets(nums, i + 1, has) + generateSubsets(nums, i + 1,curr)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        return generateSubsets(nums, 0,[])

