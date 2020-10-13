n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    if data.__len__() != m:
        print("Wrong Input!")
        exit()
    minValue = min(data)
    if minValue > result:
        result = min(data)

print(result)
