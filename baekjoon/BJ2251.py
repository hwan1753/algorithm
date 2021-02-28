# import sys
#
# array = list(map(int,sys.stdin.readline().split()))
# result = []
# idx = 0
# while idx < 5:
#     a = array[0]
#     b = array[1]
#     c = array[2]
#     temp = 0
#     if idx == 0:
#         # 1번 경우
#         if array[1] >= array[2]:
#             result.append(0)
#         else:
#             result.append(c-b)
#     elif idx == 1:
#         # 2번 경우
#         if array[1] >= array[2]:
#             b = c
#             c = 0
#             if array[0] >= array[1]:
#                 a = b
#                 b = 0
#                 result.append(a)
#             else:
#                 b = b - a
#                 result.append(a)
#         else:
#             c = c - b
#             if array[0] >= array[1]:
#                 a = b
#                 b = 0
#                 c = a + c
#                 a = 0
#                 result.append(c)
#
#             else:
#                 b = b - a + c
#                 c = a
#                 a = 0
#                 result.append(c)
#
#     elif idx == 2:
#         # 3번
#         if array[0] >= array[2]:
#             result.append(0)
#         else:
#             result.append(c-a)
#
#     elif idx == 3:
#         # 4번
#         if array[1] >= array[2]:
#             result.append(c)
#         else:
#             c = c - b
#             if array[0] >= array[2]:
#                 result.append(b)
#             else:
#                 if array[0] >= array[1]:
#                     result.append(c)
#                 else:
#                     result.append(c - a + b)
#     elif idx == 4:
#         # 5번
#         result.append(c)
#
#     idx += 1
#
# # result = sorted(set(result))
#
# answer = ''
# for num in range(len(result)):
#     answer += str(result[num])
#     if num != len(result) - 1:
#         answer += ' '
#
# print(answer)
#

chk = [[0] * 201 for i in range(201)]
a = [[0] * 201]
print(chk[2])
print(a)