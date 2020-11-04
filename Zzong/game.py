n, m = map(int, input().split())
x, y, direct = map(int, input().split())
h = [[0]*m for _ in range(n)]
h[x][y] = 1
array = []
hx = x
hy = y
for i in range(n):
    array.append(list(map(int, input().split())))

def turnleft():
    global direct
    if direct == 0:
        direct = 3
    else:
        direct -= 1

count = 1
turncount = 0
while 1:
    turnleft()
    if direct == 0:
        hx = x-1
    elif direct == 1:
        hy = y+1
    elif direct == 2:
        hx = x+1
    else:
        hy = y-1
    if h[hx][hy] == 0 and array[hx][hy] == 0:
        h[hx][hy] == 1
        x = hx
        y = hy
        count += 1
        turncount = 0
        continue
    else :
        turncount += 1
    if turncount == 4:
        if direct == 0:
            hx = x-1
        elif direct == 1:
            hy = y+1
        elif direct == 2:
            hx = x+1
        else:
            hy = y-1
        if array[hx][hy] == 1:
            break
        else:
            x = hx
            y = hy
        turncount = 0
    
print(count)

