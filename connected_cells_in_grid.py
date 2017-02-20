# Consider a matrix with  rows and  columns, where each cell contains either a  or a  and any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally; in other words, cell  is connected to cells , , , , , , , and , provided that the location exists in the matrix for that .

# If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

# Task 
# Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

# Input Format

# The first line contains an integer, , denoting the number of rows in the matrix. 
# The second line contains an integer, , denoting the number of columns in the matrix. 
# Each line  of the  subsequent lines contains  space-separated integers describing the respective values filling each row in the matrix.

# Constraints

# Output Format

# Print the number of cells in the largest region in the given matrix.

# Sample Input

# 4
# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0
# Sample Output

# 5
# Explanation

# The diagram below depicts two regions of the matrix; for each region, the component cells forming the region are marked with an X:

# X X 0 0     1 1 0 0
# 0 X X 0     0 1 1 0
# 0 0 X 0     0 0 1 0
# 1 0 0 0     X 0 0 0
# The first region has five cells and the second region has one cell. Because we want to print the number of cells in the largest region of the matrix, we print .


from collections import deque
def is_legal(pos, grid):
    if pos[0] >= len(grid) or pos[0] < 0:
        return False
    elif pos[1] >= len(grid[0]) or pos[1] < 0:
        return False
    else:
        return True

def bfs(start, grid):
    q = deque([start])
    size = 0
    while q:
        loc = q.popleft()
        row = loc[0]
        col = loc[1]
        if is_legal(loc, grid) and grid[row][col] == 1 :
            size +=1
            grid[row][col] = 'X'
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    q.append(row+a, col+b)
                    
    return size
            
def getBiggestRegion(grid):
    biggest_region = 0
    for row in grid:
        for col in row:
            if col == 1:
                s = dfs((grid.index(row), row.index(col)) , grid)
                biggest_region = max(s, biggest_region)
                

    return biggest_region