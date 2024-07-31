a, b = input().split()
reverse_a = ''
reverse_b = ''

data = []

for c in a:
    reverse_a = c + reverse_a
    data.append(int(reverse_a))
for c in b:
    reverse_b = c + reverse_b
    data.append(int(reverse_b))

print(max(data))