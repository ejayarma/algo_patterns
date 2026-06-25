from math import floor, sqrt

class Solution:
    def square_sum(self, target: int) -> bool:
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

solve = Solution()


print('1', solve.square_sum(1))
print('2', solve.square_sum(2))
print('3', solve.square_sum(3))
print('4', solve.square_sum(4))
print('5', solve.square_sum(5))
print('6', solve.square_sum(6))
print('7', solve.square_sum(7))
print('8', solve.square_sum(8))
