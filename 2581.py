n = int(input())
m = int(input())
index = 0
a = [False, False] + [True]*(m-1)

primes=[]

for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

for i in primes:
    if i >= n:
       index = primes.index(i)
       break
        

del primes[0:index]
print(sum(primes))
print(primes[0])