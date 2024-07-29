import sys

n = sys.stdin.readline().rstrip().split('-')
temp = []

for i in n:
    count = 0
    for j in i.split('+'):
        count += int(j)
    temp.append(count)

result = temp[0]
for i in temp[1:]:
    result -= i

print(result)
