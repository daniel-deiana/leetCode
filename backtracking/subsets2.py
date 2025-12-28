from copy import copy

def computeFreqMap(nums):
    freqMap = {}
    for n in nums:
        freqMap[n] = freqMap.get(n,0) + 1
    return freqMap

def hasSameFreq(a: dict, b : dict):
    for key in a.keys():
        if key not in b or b[key] != a[key]:
            return False
    
    for key in b.keys():
        if key not in a or b[key] != a[key]:
            return False
    
    return True

def isDuplicateSubset(mySubset,subsets):
    for subset in subsets: 
        freqMap = computeFreqMap(mySubset)
        if hasSameFreq(freqMap, computeFreqMap(subset)):
            return True
    return False


def generateSubsetWithDuplicate(nums, curr, subsets):
    if len(nums) == len(curr):
        if not isDuplicateSubset(curr,subsets): subsets.append(curr)
        return 
    
    availables = copy(nums)
    for p in curr:
        if p in availables: availables.remove(p)


    if not isDuplicateSubset(curr,subsets):
        subsets.append(curr)

    for p in availables:
        generateSubsetWithDuplicate(nums, curr + [p], subsets)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        generateSubsetWithDuplicate(nums, [], subsets)
        return subsets
