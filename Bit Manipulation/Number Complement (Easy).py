# 476. Number Complement - Easy
# Tags - Bit Manipulation

class Solution:
    def findComplement(self, num: int) -> int:
        bnum = 2**len(bin(num)[2:]) - 1
        return num^bnum