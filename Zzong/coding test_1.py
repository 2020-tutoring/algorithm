n = map(int, input().split())
count = 0

for i in [500,100,50,10]:
    count += n//i
    n %= i
print(count)