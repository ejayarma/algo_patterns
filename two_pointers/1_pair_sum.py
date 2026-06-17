def pair_sum_brute_force(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def pair_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        result = nums[left] + nums[right]
        if result < target:
            left += 1
        elif result > target:
            right -= 1
        else:
            return [left, right]
    return []


# TEST CASES
print("nums = [], target = 0: ", pair_sum_sorted([], 0), end='\n')
print("nums = [1],target = 1: ", pair_sum_sorted([1], 1), end='\n')
print("nums = [2, 3],target = 5: ", pair_sum_sorted([2, 3], 5), end='\n')
print("nums = [2, 4],target = 5: ", pair_sum_sorted([2, 4], 5), end='\n')
print("nums = [2, 2, 3],target = 5: ", pair_sum_sorted([2, 2, 3], 5), end='\n')
print("nums = [-1, 2, 3],target = 2: ", pair_sum_sorted([-1, 2, 3], 2), end='\n')
print("nums = [-3, -2, -1],target = -5: ", pair_sum_sorted([-3, -2, -1], -5), end='\n')

