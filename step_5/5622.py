str = input()
data = ['', "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", '']

count = 0
for i in data:
    for j in str:
        if j in i:
            count += (data.index(i)+2)

print(count)