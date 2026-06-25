def zero_striping_hash_sets(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
        
    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

    print(matrix)

def zero_striping_hash_sets_improved(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False
    
    for r in range(m):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break
        
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
        
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
                
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if first_row_has_zero:
        for c in range(n):
            matrix[0][c] = 0
            
    if first_col_has_zero:
        for r in range(m):
            matrix[r][0] = 0
            
    print(matrix)
