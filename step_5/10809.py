s = input()

data = []
for i in range(97, 123):
    if chr(i) not in s:
        data.append(-1)
    else:
        data.append(s.index(chr(i)))

print(*data)