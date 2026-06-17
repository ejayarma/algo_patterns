def triplet_sum_brute_force(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(
                        sorted([nums[i], nums[j], nums[k]])
                    )
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]


def pair_sum_sorted_all_pairs(nums: list[int], target: int, start: int) -> list[list[int]]:
    left, right = start, len(nums) - 1
    pairs = []
    while left < right:
        result = nums[left] + nums[right]
        if result == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif result < target:
            left += 1
        else:
            right -= 1
        
    return pairs


def triplet_sum_sorted(nums: list[int]) -> list[list[int]]:
    all_triplets = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pairs = pair_sum_sorted_all_pairs(nums, -nums[i], i + 1)
        all_triplets.extend([nums[i], *pair] for pair in pairs)
    return all_triplets


print("nums = []: ", triplet_sum_sorted([]))
print("nums = [0]: ", triplet_sum_sorted([0]))
print("nums = [1, -1]: ", triplet_sum_sorted([1, -1]))
print("nums = [0, 0, 0]: ", triplet_sum_sorted([0, 0, 0]))
print("nums = [1, 0, 1]: ", triplet_sum_sorted([1, 0, 1]))
print("nums = [0, 0, 1, -1, 1, -1]: ", triplet_sum_sorted([0, 0, 1, -1, 1, -1]))
print("nums = [-4, -4, -2, 0, 0, 1, 2, 3]: ", triplet_sum_sorted([-4, -4, -2, 0, 0, 1, 2, 3]))