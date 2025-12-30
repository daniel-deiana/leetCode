from copy import copy 


def isPalindrome(s):
    
    if len(s) == 0:
        return False
    
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]: return False
        l = l + 1
        r = r - 1

    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start,curr):
            
            if start == len(s):
                result.append(copy(curr))
            

            for i in range(start,len(s)+1):
                if isPalindrome(s[start:i]):
                    curr.append(s[start:i])
                    backtrack(i,curr)
                    curr.pop()

        backtrack(0,[])        
        return result
