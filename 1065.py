n = int(input())
count = 0

if n >= 100:
    for i in range(100, n+1):
        i_str = str(i)
        if (int(i_str[1]) - int(i_str[0])) == (int(i_str[2]) - int(i_str[1])):
            count += 1
    print(count+99)
else:
    print(n)

