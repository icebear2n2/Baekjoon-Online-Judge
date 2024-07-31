data = []
for i in range(10):
    data.append(int(input()) % 42)

set_data = set(data)
print(len(set_data))