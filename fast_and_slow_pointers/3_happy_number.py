def get_next_num(n: int) -> int:
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit ** 2
    return result


def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        elif slow == fast:
            return False

print(get_next_num(23))