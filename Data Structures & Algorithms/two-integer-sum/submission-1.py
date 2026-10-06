class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = {}
        for key, value in enumerate(nums):
            final[value] = key
        print(final)
        for key, value in enumerate(nums):
            diff = target - value
            if diff in final and final[diff] != key:
                return [key, final[diff]]
        return[]