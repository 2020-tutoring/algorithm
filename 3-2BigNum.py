n, m, k = map(int, input().split())
data = list(map(int, input().split()))
if data.__len__() != n:
    print("Wrong Input!")
    exit()
data.sort(reverse=True)
result = 0

while True:
    for j in range(k - 1):
        result += data[0]
        m -= 1
        if m == 0:
            break
    if m == 0:
        break
    result += data[1]
    m -= 1

print(result)