class Solution283:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return 0
        offset = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[offset] = nums[i]
                offset = offset + 1
        for i in range(offset, len(nums)):
            nums[i] = 0