def two_sum(nums, target):

    num_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

    return []
print(two_sum([2,5,6,1,5,6,8],10))