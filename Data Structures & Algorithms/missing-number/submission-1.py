class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumAll = len(nums) * (len(nums)+1) //2
        for num in nums:
            sumAll -= num
        return sumAll