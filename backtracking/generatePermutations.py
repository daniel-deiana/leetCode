from copy import copy

def generatePermutations( nums, curr, permutations):
    if len(curr) == len(nums):
        permutations.append(curr)
        return

    # generate a new object instead of increasing reference count of nums
    availables = copy(nums)
    for p in nums:
        if p in curr: availables.remove(p)

    for p in availables:
        generatePermutations(nums, curr + [p], permutations)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        generatePermutations(nums, [], permutations)
        return permutations        
