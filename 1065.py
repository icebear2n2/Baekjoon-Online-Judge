# import sys

# n = int(sys.stdin.readline())
# n1 = 0
# num = 0

# for i in range(1, n+1):
#     if i >= 1 and i < 100:
#         num+=1
#         print(i)
#     else:
#         i = str(i)
#         try:
#             n1 = int(i[0]) + (1 % (int(i[0]) - int(i[2]))) - int(i[0])
#             if n1 <= 0:
#                 continue
#             else:
#                 print(i)
#                 print(n1)
#                 num += 1
#         except ZeroDivisionError:
#             n1 = int(i[0]) + ((int(i[0]) - int(i[2])) % 1) - int(i[0])
#             if n1 <= 0:
#                 continue
#             else:
#                 print(i)
#                 print(n1)
#                 num += 1
# print(num)
