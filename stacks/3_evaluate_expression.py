def evaluate_expression(s: str) -> int:
    stack = []
    curr_num, sign, res = 0, 1, 0
    for c in s:
        if c.isdigit():
            curr_num = int(c) + 10 * curr_num
        elif c == '-' or c == '+':
            res += curr_num * sign
            curr_num = 0
            sign = -1 if c == '-' else 1
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif c == ')':
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
        else:
            continue


    return res + curr_num * sign

print(evaluate_expression('18-(7-(2-4) )'))
