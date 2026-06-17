def shift_zeros_to_the_end_naive(nums: list[int]) -> None:
    temp = [0] * len(nums)
    i = 0
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1
    for j in range(len(nums)):
        nums[j] = temp[j]
    print(nums)
    
    
def shift_zeros_to_the_end_best(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    print(nums)


def shift_zeros_to_the_end_mine(nums: list[int]) -> None:
    n = len(nums)
    left, right = 0, 1
    while left < right < n:
        if not nums or n <= 2:
            break
        while (left < right < n) and nums[left] != 0:
            left += 1
        while (left < right < n) and nums[right] == 0:
            right += 1
        if (left < right < n) and nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right += 1
    print(nums)


def shift_zeros_to_the_end_best(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    print(nums)


shift_zeros_to_the_end_best([])
shift_zeros_to_the_end_best([0])
shift_zeros_to_the_end_best([1])
shift_zeros_to_the_end_best([0, 0, 0])
shift_zeros_to_the_end_best([1, 3, 2])
shift_zeros_to_the_end_best([1, 1, 1, 0, 0])
shift_zeros_to_the_end_best([0, 0, 1, 1, 1])
shift_zeros_to_the_end_best([0, 1, 0, 3, 2])
