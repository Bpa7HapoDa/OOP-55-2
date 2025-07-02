def two_sum(nums, target):

    num_map = {}

    for index, num in enumerate(nums):
        found = target - num
        if found in num_map:
            return [num_map[found], index]
        num_map[num] = index

    return []
print(two_sum([2,5,6,1,5,6,8],10))