# 총 금액
X = int(input())

# 물건 개수
N = int(input())
result=0

for i in range(1, N+1):
    A,B = map(int, input().split())
    result+=(A*B)

if ( result == X ):
    print("Yes")
else:
    print("No")