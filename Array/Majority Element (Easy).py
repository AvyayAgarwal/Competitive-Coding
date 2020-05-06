# 169. Majority Element
# Tags - Array, Divide and Conquer, Bit Manipulation


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

        # HashMap method
        # countMap = collections.Counter(nums)
        # occurences = len(nums) // 2
        # print(countMap)
        # for i in countMap:
        #     if(countMap[i] > occurences):
        #         return i