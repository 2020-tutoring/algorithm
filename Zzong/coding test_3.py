n, m = map(int, input().split())

mn = 0
result = 0

for i in range(n):
    array = list(map (int, input().split()))
    mn = min(array)
    result = max(result, mn)
    
print(result)