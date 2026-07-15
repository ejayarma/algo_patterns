def valid_parentheses_expression(s: str) -> bool:
    stack = []
    parentheses_map = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    for c in s:
        if c in parentheses_map:
            stack.append(c)
        else:
            if stack[-1] == parentheses_map[c]:
                stack.pop()
            else:
                return False
    
    return not stack
