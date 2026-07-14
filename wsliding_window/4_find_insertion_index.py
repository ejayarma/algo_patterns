def find_the_insertion_index(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
            
    return left

print(find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 4))
print(find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 6))

