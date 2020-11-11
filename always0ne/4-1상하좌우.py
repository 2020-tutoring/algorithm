n = int(input())
x,y = 1,1
paths = input().split()

for path in paths:
    if path == 'L'and y>1:
        y-=1
    elif path == 'R' and y<n:
        y+=1
    elif path == 'U' and x>1:
        x-=1
    elif path == 'D' and x<n:
        x+=1

print(x,y)