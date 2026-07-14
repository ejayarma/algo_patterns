def find_the_target_in_rotated_sorted_arr(nums : list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[left] <= target:
            if nums[left] <= target < mid:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            
    return left if nums and nums[left] == target else -1
