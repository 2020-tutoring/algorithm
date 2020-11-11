from collections import deque

n,m = map(int, input().split())
mm = []
for i in range(n):
    mm.append(list(map(int, input())))

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if mm[nx][ny] == 0:
                continue
            if mm[nx][ny] == 1:
                mm[nx][ny] = mm[x][y]+1
                queue.append((nx,ny))

    return mm[n-1][m-1]

print(bfs(0,0))