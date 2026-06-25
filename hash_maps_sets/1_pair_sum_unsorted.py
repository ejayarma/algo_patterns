def pair_sum_unsorted_brute_force(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def pair_sum_unsorted_two_passes(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [i, nums_map[complement]]
        
    return []


def pair_sum_unsorted_one_pass(nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [i, nums_map[complement]]
        nums_map[num] = i
        
    return []


print("nums = [], target = 3, output =", pair_sum_unsorted_one_pass([], 3))
print("nums = [0], target = 3, output =", pair_sum_unsorted_one_pass([0], 3))
print("nums = [-1, 3, 4, 3], target = 3, output =", pair_sum_unsorted_one_pass([-1, 3, 4, 3], 3))
