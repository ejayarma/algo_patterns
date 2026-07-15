def largest_num_to_right_brute_force(nums: list[int]) -> list[int]:
    n = len(nums)
    res = []
    for i in range(n):
        found = False
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                found = True
                res.append(nums[j])
                break
        if not found:
            res.append(-1)
        
    return res



def largest_num_to_right_stack(nums: list[int]) -> list[int]:
    res = []
    stack = []
    for i in reversed(range(len(nums))):
        curr_val = nums[i]
        while stack and stack[-1] <= curr_val:
            stack.pop()
        if stack:
            res.insert(0, stack[-1])
        else:
            res.insert(0, -1)
        stack.append(curr_val)
    
    return res

def largest_num_to_the_right(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res


print(largest_num_to_right_stack([5, 2, 4, 6, 1]))