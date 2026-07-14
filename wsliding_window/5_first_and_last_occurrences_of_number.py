def first_and_last_occurrences_of_number(nums: list[int], target: int) -> list[int]:
    upper_bound = upper_bound_binary_search(nums, target)
    lower_bound = lower_bound_binary_search(nums, target)
    
    return [lower_bound, upper_bound]
    
def lower_bound_binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums and nums[left] == target else -1
            
    
def upper_bound_binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid  
    return right if nums and nums[right] == target else -1


print(first_and_last_occurrences_of_number([1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], 4))
