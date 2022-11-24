
n = int(input())

lst = list(map(int, input().split()))
lst.sort()

count = 0

a = [False,False] + [True]*(lst[-1]-1)
primes = []

for i in range(2,lst[-1]+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, lst[-1]+1, i):
            a[j] = False

for i in lst:
    if i in primes:
        count += 1

print(count)