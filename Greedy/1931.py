n = int(input())
end_point: int = 0
answer: int = 0

arr = []

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

arr.sort(key=lambda x: (x[1], x[0]))

for new_start, new_end in arr:
    if end_point <= new_start: # end_point보다 new_start가 같거나 커야함(Ex. end_point: 4, new_start: 5)
        answer += 1
        end_point = new_end

print(answer)