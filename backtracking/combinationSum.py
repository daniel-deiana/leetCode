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

def generateCombinationSum(nums, curr, i, subsets ,target):
    
    if sum(curr) > target:
        # exceeded the target, stop
        return

    if sum(curr) == target:
        # check if the frequence dictionary is already the same of one of the subsets
        myFreqMap = computeFreqMap(curr)
        isDuplicate = False
        for subset in subsets:
            freqMap = computeFreqMap(subset)
            if hasSameFreq(myFreqMap,freqMap):
                isDuplicate = True    

        if not isDuplicate:
            subsets.append(curr)

    for num in nums:
        generateCombinationSum(nums, curr + [num], i + 1, subsets, target)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        generateCombinationSum(nums, [], 0,  subsets, target)
        return subsets
