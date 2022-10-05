chess_piece=[1, 1, 2, 2, 2, 8]

lst = list(map(int, input().split()))
result=[]
for i in range(0, len(chess_piece)):
    print(chess_piece[i] - lst[i])