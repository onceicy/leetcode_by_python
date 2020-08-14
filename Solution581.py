class Solution581:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = nums[:]
        snums.sort()
        left = len(nums)
        right = 0
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                left = min(left,i)
                right = max(right,i)
        if right-left+1 > 0:
            return right-left+1
        return 0