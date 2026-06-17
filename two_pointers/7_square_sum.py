from math import floor, sqrt

def square_sum(target: int) -> bool:
    right = floor(sqrt(target))
    left = -right
    while left < right:
        acc = left ** 2 + right ** 2
        if acc < target:
            left += 1
        elif acc > target:
            right -= 1
        else:
            return True
    return False

print('1', square_sum(1))
print('2', square_sum(2))
print('3', square_sum(3))
print('4', square_sum(4))
print('5', square_sum(5))
print('6', square_sum(6))
print('7', square_sum(7))
print('8', square_sum(8))


