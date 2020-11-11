n, m = map(int, input().split())
frame = []
for i in range(n):
    frame.append(list(map(int, input())))

def dfs(x, y):
    if x>=n or x<0 or y>=m or y<0:
        return 0
    if frame[x][y] == 0:
        frame[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return 1
    return 0

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == 1:
            result += 1

print(result)