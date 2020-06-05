# 528. Random Pick with Weight - Medium
# Tags - Binary Search, Random

class Solution:

    def __init__(self, w: List[int]):
        self.nums = [w[0]]
        for i in range(1, len(w)):
            self.nums.append(w[i] + self.nums[-1])
            
    def binSearch(self, val):
        l = 0
        r = len(self.nums) - 1
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] < val:
                l = mid + 1
            else:
                r = mid     
        return l

    def pickIndex(self) -> int:
        return self.binSearch(random.randrange(1, self.nums[-1] + 1))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()