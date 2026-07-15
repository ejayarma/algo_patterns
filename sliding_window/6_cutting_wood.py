def cutting_wood(heights: list[int], k: int) -> int:
    left, right = 0, max(heights)
    while left < right:
        mid = left + (right - left) // 2 + 1
        if cuts_enough_wood( mid, k, heights):
            left = mid
        else:
            right = mid - 1
    return right

def cuts_enough_wood(H: int, k: int, heights: list[int]) -> bool:
    wood_collected = 0
    for height in heights:
        if height > H:
            wood_collected += (height - H)
    return wood_collected >= k


print(cutting_wood([2, 6, 3, 8], 7))
