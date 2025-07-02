import time # used only for measuring the solution

def next_id(direction,cursor):
    # Movement patterns: (row_change, column_change) for right, down, left, up
    direction_change = [(0,1),(1,0),(0,-1),(-1,0)]
    row_change, col_change = direction_change[direction]
    row = cursor[0] + row_change
    col = cursor[1] + col_change
    return (row,col)


def spiralOrder(matrix,start_pos = (0,0)):
    # Handle empty or single row/column matrices
    if len(matrix) == 0:  # []
        return []
    if len(matrix) == 1:  # [[1,2,3]]
        return matrix[0]
    if len(matrix[0]) == 1:  # [[1],[2],[3]]
        out = []
        for row in matrix:
            out.append(row[0])
        return out

    Mx = len(matrix[0])  # width
    My = len(matrix)     # height
    AmountOfItems = Mx*My
    direction = 0  # 0=right, 1=down, 2=left, 3=up
    recordedIndexes = set()  # visited positions
    out:list = []
    cursor = start_pos

    for i in range(AmountOfItems):
        next_pos = next_id(direction,cursor)
        
        # Change direction if we hit a wall or visited position
        if next_pos[0] < 0 or next_pos[0] >= My or next_pos[1] < 0 or next_pos[1] >= Mx or next_pos in recordedIndexes:
            direction = (direction + 1)%4
            next_pos = next_id(direction,cursor)
            
        recordedIndexes.add(cursor)
        out.append(matrix[cursor[0]][cursor[1]])
        cursor = next_pos
    return out

if __name__ == "__main__": 
    import tester
    from Cases import SPIRAL_MATRIX_TEST_CASES
    
    tester.run_tests(
        cases=SPIRAL_MATRIX_TEST_CASES,
        test_function=spiralOrder,
        function_name="spiralOrder"
    )