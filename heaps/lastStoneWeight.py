import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush_max(h,stone)
        S
        while len(h) > 1:
            x = heapq.heappop_max(h)
            y = heapq.heappop_max(h)
            if x < y:
                heapq.heappush_max(h,y-x)
            elif x > y:
                heapq.heappush_max(h,x-y)
        
        if len(h):
            return heapq.heappop_max(h)
        else:
            return 0

