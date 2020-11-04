n = input()
r = int(n[1])
c = int(ord(n[0])-96)

move = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)]
case = 0

for i in move:
    nr = r+i[0]
    nc = c+i[1]
    if(nr <= 8 and nr >=1 and nc <= 8 and nc >= 1):
        case += 1
print(case)