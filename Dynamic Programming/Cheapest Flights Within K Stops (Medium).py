# 787. Cheapest Flights Within K Stops - Medium
# Tags - Dynamic Programming (DP), Heap, Breadth-first Search (BFS)

# Note - Sample solution plugged from discussion board ... TODO: Think of proper solution later

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        srcmap = collections.defaultdict(list)
        checkmap = collections.defaultdict(lambda: float('inf'))
        for u, v, c in flights:
            srcmap[u] += [(v, c)]
    
        q = [(src, -1, 0)]
        
        while q:
            pos, k, cost = q.pop(0)
            if pos == dst or k == K:
                continue 
            for nei, p in srcmap[pos]:
                if cost + p >= checkmap[nei]:
                    continue
                else:
                    checkmap[nei] = cost+p
                    q += [(nei, k+1, cost+p)]
                
        return checkmap[dst] if checkmap[dst] < float('inf') else -1
		