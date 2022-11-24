n = int(input())
m = int(input())

a = [False, False] + [True]*(m-1)


primes = []
result = []
for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

while m > n:
    n += 1
    if n in primes:
        result.append(n)
    else:
        continue

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])