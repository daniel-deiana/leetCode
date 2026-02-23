import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        h = []
        
        if len(points) == 0:
            return h

        for point in points:
            distance = point[0]**2 + point[1]**2
            if len(h) < k:
                heapq.heappush_max(h,(distance,point[0],point[1]))
                continue
            elif distance < h[0][0]:
                    heapq.heappop_max(h)   
                    heapq.heappush_max(h,(distance,point[0],point[1]))

        return [[el[1],el[2]] for el in h]
