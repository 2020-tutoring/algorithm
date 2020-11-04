n = int(input())
road = input().split()

x = 1
y = 1

nx = x
ny = y

for i in road:
    if(i == 'L'):
        ny = y-1
    elif(i == 'R'):
        ny = y+1
    elif(i == 'U'):
        nx = x-1
    else:
        nx = x+1
    if(nx < 1 or nx > n or ny < 1 or ny > n):
        continue
    x = nx
    y = ny
    
print(x,y)