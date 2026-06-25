from collections import defaultdict, Counter

def geometric_sequence_triplets_mine(nums: list[int], r: int) -> int:
    
    count = 0
    if not nums:
        return count
    
    left_map = {}
    right_map = {}
    
    for x in nums:
        right_map[x] = right_map.get(x, 0) + 1
    
    for x in nums:
        right_map[x] = right_map.get(x, 0) - 1
        if x % r == 0:
            count += left_map.get(x // r, 0) * right_map.get(x * r, 0)
        left_map[x]  = left_map.get(x, 0) + 1
    return count

def geometric_sequence_triplets(nums: list[int], r: int) -> int:
    
    count = 0
    if not nums:
        return count
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    
    for x in nums:
        right_map[x] += 1
    
    for x in nums:
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        left_map[x] += 1
    return count

print(geometric_sequence_triplets([2, 1, 2, 4, 8, 8], 2))
