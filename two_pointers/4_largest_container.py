def largest_container_brute_force(heights: list[int]) -> int:
    max_water = 0
    n = len(heights)
    for i in range(n):
        for j in range(i + 1, n):
            height = min(heights[i], heights[j])
            water = height * (j - i)
            print("Height:", height)
            max_water = max(max_water, water)
    return max_water


# print("heights = [2, 7, 8, 3, 7, 6]:", largest_container_brute_force([2, 7, 8, 3, 7, 6]))

def largest_container(heights: list[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(water, max_water)
        
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
        
    return max_water

print("heights = []:", largest_container([])) # empty array
print("heights = [1]:", largest_container([1])) # one element
print("heights = [0, 1, 0]:", largest_container([0, 1, 0])) # no containers that can contain water
print("heights = [3, 3, 3, 3]:", largest_container([3, 3, 3, 3])) # equal heights
print("heights = [1, 2, 3]:", largest_container([1, 2, 3])) # strictly increasing heights
print("heights = [3, 2, 1]:", largest_container([3, 2, 1])) # strictly decreasing heights
print("heights = [2, 7, 8, 3, 7, 6]:", largest_container([2, 7, 8, 3, 7, 6])) # different heights
