n, m, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0

array.sort()

"""while True:
    for i in range(k):
        if m == 0:
            break
        result += array[n-1]
        m -= 1
    if m == 0:
        break
    result += array[n-2]
    m -= 1
"""

mx = int(m/(k+1))*k*array[n-1]
my = int(m/(k+1))*array[n-2]
mz = int(m%(k+1))*k
result = mx+my+mz

print(result)