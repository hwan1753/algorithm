arr = list(str(input()))


idx = 0
stack = []
a = False

for i in arr:
    val = []
    if i == ")":
        while stack:
            chk = stack.pop()
            if chk == "(":
                if val:
                    num = 2 * sum(val)
                else:
                    num = 2
                stack.append(num)
                break
            elif chk == "[":
                a = True
                break
            else:
                val.append(chk)
        if not stack:
            a = True
            break
    elif i == "]":
        while stack:
            chk = stack.pop()
            if chk == "[":
                if val:
                    num = 3 * sum(val)
                else:
                    num = 3
                stack.append(num)
                break
            elif chk == "(":
                a = True
                break
            else:
                val.append(chk)
        if not stack:
            a = True
            break
    else:
        stack.append(i)

if "(" in stack or "[" in stack or a:
    print(0)
else:
    print(sum(stack))
#
#
#     elif i == "]":
#
#     else:
#         stack.append(i)
# while queue:
#     v = queue.popleft()
#     if not tmp:
#         tmp.append(v)
#     else:
#         if tmp[-1] == "(" and v == ")":
#             if val:
#                 num = 2*sum(val)
#             else:
#                 num = 2
#             val = []
#             tmp.pop()
#             tmp.append(num)
#         elif tmp[-1] == "(" and str(v).isnumeric():
#             val.append(v)
#         elif tmp[-1] == "[" and v == "]":
#             if val:
#                 num = 3 * sum(val)
#             else:
#                 num = 3
#             val = []
#             tmp.pop()
#             tmp.append(num)
#         elif tmp[-1] == "[" and str(v).isnumeric():
#             val.append(v)
#
#         else:
#             tmp.extend(val)
#             tmp.append(v)
#             val = []
#
#     if len(queue) == 0:
#         if "(" in tmp or "[" in tmp:
#             queue = deque(tmp)
#             tmp = []
#             val = []
#         else:
#             print(sum(tmp))
#
# idx = 0