# 1029. Two City Scheduling - Easy
# Tags - Greedy

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        N = len(costs)//2
        cost = 0
        for a,b in costs:
            if N > 0:
                cost += a
            else:
                cost += b
            N -= 1
        return cost