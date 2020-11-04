n = int(input())
count = 0
for i in range(n+1):
    if(i == 3):
        for m in range(60):
            for s in range(60):
                count += 1
    else:
        for m in range(60):
            if('3' in str(m)):
                for s in range(60):
                    count += 1
            else:
                for s in range(60):
                    if('3' in str(s)):
                        count += 1
print(count)