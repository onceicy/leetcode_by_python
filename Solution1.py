class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number1 in range(len(nums)):
            for number2 in range(number1+1,len(nums)):
                if nums[number1] + nums[number2] == target:
                    return [number1, number2];