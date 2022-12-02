n, m = map(int, input().split())
def factorization(n, m):

    lst = []
    num = 0
    for i in range(n, m+1):
        d = 2
        while d <= i:
            if i % d == 0:
                if d in lst:
                    break
                i = i / d
                num = d
                if num < n:
                    break
                print(num)
                lst.append(num)
            else:
                d = d + 1
factorization(n, m) 

