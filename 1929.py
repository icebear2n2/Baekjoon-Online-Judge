n, m = map(int, input().split())

lst = []

def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            if d in lst:
                break
            else:
                if d < n:
                    break
                else:
                    lst.append(d)
                    print(d)
            x = x / d
        else:
            d = d + 1

for i in range(n, m+1):
    factorization(i) 

