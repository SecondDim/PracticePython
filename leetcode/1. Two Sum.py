class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = {}
        for i, x in enumerate(nums):
            dnums[x] = i

        for i, x in enumerate(nums):
            j = dnums.get(target - x)
            if j != None and i != j:
                return [i, j]

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
