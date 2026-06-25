def longest_chain_of_consecutive_numbers_brute_force(nums: list[int]) -> int:
    if not nums:
        return 0
    
    longest_chain = 0
    
    for num in nums:
        curr_num = num
        curr_chain = 1
        while(curr_num + 1 in nums):
            curr_num += 1
            curr_chain += 1
        longest_chain = max(longest_chain, curr_chain)

    return longest_chain


def longest_chain_of_consecutive_numbers_hash(nums: list[int]) -> int:
    if not nums:
        return 0
    
    longest_chain = 0
    nums_set = set(nums)
    
    for num in nums:
        curr_num = num
        curr_chain = 1
        if curr_num - 1 not in nums_set:
            while(curr_num + 1 in nums_set):
                curr_num += 1
                curr_chain += 1
            longest_chain = max(longest_chain, curr_chain)

    return longest_chain


def longest_chain_of_consecutive_numbers_no_hash(nums: list[int]) -> int:
    if not nums:
        return 0
    
    if len(nums) == 1:
        return 1
    
    current_chain = 1
    longest_chain = 0
    
    nums.sort()
                
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            current_chain += 1
            longest_chain = max(longest_chain, current_chain)
        else:
            current_chain = 1
    return max(longest_chain, current_chain)

print(longest_chain_of_consecutive_numbers_hash([1, 3]))
print(longest_chain_of_consecutive_numbers_hash([1, 6, 2, 5, 8, 7, 10, 3]))
