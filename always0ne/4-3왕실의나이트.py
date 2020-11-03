input_xy = input()
column = int(ord(input_xy[0])) - int(ord('a')) + 1
row = int(input_xy[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        cnt += 1

print(cnt)

