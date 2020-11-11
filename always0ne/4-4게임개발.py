n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
visited[x][y] = 1

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn = 0
while True:
    direction -= 1
    if direction == -1:
        direction = 3
    new_x = x + dx[direction]
    new_y = y + dy[direction]
    if visited[new_x][new_y] == 0 and game_map[new_x][new_y] == 0:
        visited[new_x][new_y] = 1
        x = new_x
        y = new_y
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        new_x = x - dx[direction]
        new_y = y - dy[direction]
        if game_map[new_x][new_y] == 0:
            x = new_x
            y = new_y
        else:
            break
        turn = 0

print(cnt)