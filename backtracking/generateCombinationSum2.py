
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

# We want to compute the combination by using the available elements
# Each time we generate a new combination we restrict the availables elements to use
def generateCombinationSum2(candidates, current, target, subsets):

    if sum(current) > target:
        return

    # we check if the target matches the sum of current and if is not already present in subsets
    if sum(current) == target and not isDuplicateSubset(current,subsets):
        subsets.append(current)

    # compute the remaining elements you can use to generate other subsets
    availables = [] + candidates
    tempcurrent = [] + current
    for el in candidates:
        if el in tempcurrent and el in availables:
            availables.remove(el)
            tempcurrent.remove(el)

    # We generate combination recursively using the remaining elements that we have not used yet
    for candidate in availables:
        generateCombinationSum2(candidates, current + [candidate], target, subsets)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        generateCombinationSum2(candidates, [], target, subsets)
        return subsets
