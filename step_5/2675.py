t = int(input())

for i in range(t):
    r, s = input().split()
    str = ""
    for j in s:
        str += (j*int(r))
    print(str)