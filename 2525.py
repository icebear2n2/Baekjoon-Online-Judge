H, M = map(int, input().split())
T = int(input())

SUM = M + T

if (SUM >= 60):
    if (SUM % 60 == 0):
        H += (SUM // 60)
        SUM %= 60
        if (H >= 24):
            H -= 24
            print(H, SUM)
        else:
            print(H, SUM)
    else:
        H += (SUM // 60)
        SUM %= 60
        if (H >= 24):
            H -= 24
            print(H, SUM)
        else:
            print(H, SUM)
else:
    if (H >= 24):
        H -= 24
        print(H, SUM)
    else:
        print(H, SUM)