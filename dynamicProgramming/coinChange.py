class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def collectCoinsToAmount(used, i, currentAmount):


            if i >= len(coins):
                return -1
            newAmount = currentAmount - coins[i]
            if newAmount < 0:
                return -1
            if newAmount == 0:
                return used+1

            if (used+1,newAmount) not in cache:
                cache[(used+1,newAmount)] = collectCoinsToAmount(used+1, i, newAmount)
                addCurrent = cache[(used+1,newAmount)]
            else:
                addCurrent = cache[(used+1,newAmount)]
            
            if (used,currentAmount) not in cache:
                cache[(used,currentAmount)] = collectCoinsToAmount(used, i+1, currentAmount)
                skipCurrent = cache[(used,currentAmount)]
            else:
                skipCurrent = cache[(used,newAmount)]

            if addCurrent > 0 and skipCurrent > 0:
                return min(addCurrent,skipCurrent)
            if addCurrent < 0 and skipCurrent > 0:
                return skipCurrent
            if skipCurrent < 0 and addCurrent > 0:
                return addCurrent
            if skipCurrent < 0 and addCurrent < 0:
                return -1      
        
        return collectCoinsToAmount(0,0,amount) if amount > 0 else 0

