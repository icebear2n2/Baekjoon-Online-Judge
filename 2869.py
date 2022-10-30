A, B, V = map(int, input().split())

Day = 0
num = 0

if (A - B) == 1:
    print(V - B)
else:
    while num < V:
        Day += 1
        num += (A - B)

    print(Day)
        
        
