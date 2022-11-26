n = int(input())
m = int(input())

a = [False, False] + [True]*(m-1)

primes = []
lst = []
for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

for i in range(n, m+1):
    if i in primes:
        lst.append(i)
    else:
        continue

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
