import sys

n = sys.stdin.readline().strip().split('-') # - 기준으로 괄호를 치면 최소를 만들 수 있다.
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