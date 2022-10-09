n = int(input())

for i in range(n):
    result=[]
    num, char = map(str, input().split())
    char = list(char)
    for ch in range(len(char)):
        
        for j in range(int(num)):
            result.append(char[ch])

    result = ''.join(result)
    print(result)
        