def twoSum(nums, target):
    dnums = {}
    for i, x in enumerate(nums):
        dnums[x] = i

    for i, x in enumerate(nums):
        z = target - x
        j = dnums.get(z)
        if j != None and i!=j:
            return [i, j]


print( twoSum( nums=[3,2,4], target=6 ) )
