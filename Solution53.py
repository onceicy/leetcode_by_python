class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        Max = nums[0]
        for num in nums[:]:
            if sum > 0:
                sum = sum + num
            else:
                sum = num
            Max = max(Max, sum)
        return Max