# 771. Jewels and Stones - Easy
# Tags - Hash Table

# O(mn) time
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         count = 0
#         for ch in J:
#             count += S.count(ch)
#         return count

# O(m + n) time
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        setJ = set(J)
        for ch in S:
            if(ch in setJ):
                count += 1
        return count