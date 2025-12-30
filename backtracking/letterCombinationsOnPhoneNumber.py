class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from copy import copy
        result = []
        
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wyxz"
        }

        def backtrack(i,curr):

            if len(curr) > 0 and len(curr) == len(digits):
                result.append(copy(curr))

            if i >= len(digits):
                return

            for ch in digitMap[digits[i]]:
                backtrack(i + 1, curr + ch)
        
        backtrack(0,"")
        return result
