import random # Filter connections (sequence of adjacent 1s in the 8 possible directions) and return the updated matrix 

n_rows = 5
n_cols = 5

def needs_to_be_visited(mat, i, j, visited):
    return (i >=0 and i < n_rows and j >= 0 and j < n_cols and mat[i][j] and not visited[i][j])

def DFS(mat, i, j, visited, k, count, path):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    visited[i][j] = 1
    path.append([i,j])

    for x in range(8):
        neighbor = (i + directions[x][0], j + directions[x][1])
        if needs_to_be_visited(mat, neighbor[0], neighbor[1], visited):
            DFS(mat, neighbor[0], neighbor[1], visited, k, count + 1, path)

    print path
    if (len(path) < k):
        for x in range(len(path)):
            i = path[x][0]
            j = path[x][1]
            mat[i][j] = 0 
        
    

def filter(mat, k):
    visited = [[0 for x in xrange(n_rows)] for y in xrange(n_cols)]
    count = 1
    for i in range(n_rows):
        for j in range(n_cols):
            if (mat[i][j] == 1 and visited[i][j] == False):
                # call DFS
                DFS(mat, i, j, visited, k, count, [])

    return count 

mat = [[random.choice([0,1]) for x in xrange(n_rows)] for y in xrange(n_cols)]
mat1 = [[1,0,0,1,0], [1,0,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [0,1,0,0,1]]
print mat1
filter(mat1, 8)
print mat1

# 1 0 0 1 0
# 1 0 0 0 0
# 1 1 1 1 0
# 1 0 0 0 0
# 0 1 0 0 1
