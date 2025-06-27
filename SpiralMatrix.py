import time # used only for measuring the solution

def next_id(direction,Mx,cursor):
    # Movement patterns: (row_change, column_change) for right, down, left, up
    direction_change = [(0,1),(1,0),(0,-1),(-1,0)]
    row_change, col_change = direction_change[direction]
    row = cursor[0] + row_change
    col = cursor[1] + col_change
    return (row,col)


def spiralOrder(matrix):
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
    recordedIndexes = []  # visited positions
    out:list = []
    cursor = (0,0)

    for i in range(AmountOfItems):
        next_pos = next_id(direction,Mx,cursor)
        
        # Change direction if we hit a wall or visited position
        if next_pos[0] < 0 or next_pos[0] >= My or next_pos[1] < 0 or next_pos[1] >= Mx or next_pos in recordedIndexes:
            direction = (direction + 1)%4
            next_pos = next_id(direction,Mx,cursor)
            
        recordedIndexes.append(cursor)
        out.append(matrix[cursor[0]][cursor[1]])
        cursor = next_pos
    return out

# =====================  TESTS ============================== #
print("#=======================================================#")
start_time = time.time()
testout = spiralOrder([
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
])
output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(" - test #1 Passed" if testout == output else f"test #1 Failed, Result: {testout}")
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(" - test #2 Passed" if testout == output else f"test #2 Failed, Result: {testout}")
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
  [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
  [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
  [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
  [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140],
  [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160],
  [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180],
  [181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
])
output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 161, 141, 121, 101, 81, 61, 41, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 59, 79, 99, 119, 139, 159, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 142, 122, 102, 82, 62, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 78, 98, 118, 138, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 123, 103, 83, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 97, 117, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 104, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105]
print(" - test #3 Passed" if testout == output else f"test #3 Failed, Result: "+"\n"+str(testout))
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([[1,2,3,4,5,6,7,8,9,10]])
output = [1,2,3,4,5,6,7,8,9,10]
print(" - test #4 Passed" if testout == output else f"test #4 Failed, Result: "+str(testout))
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
output = [1,2,3,4,5,6,7,8,9,10]
print(" - test #5 Passed" if testout == output else f"test #5 Failed, Result: "+str(testout))
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([[1]])
output = [1]
print(" - test #6 Passed" if testout == output else f"test #6 Failed, Result: "+str(testout))
print(f" - - Time taken: {time.time() - start_time} seconds \n")

start_time = time.time()
testout = spiralOrder([])
output = []
print(" - test #7 Passed" if testout == output else f"test #7 Failed, Result: "+str(testout))
print(f" - - Time taken: {time.time() - start_time} seconds \n")
print("#=======================================================#")