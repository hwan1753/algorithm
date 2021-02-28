from _collections import deque

def solution1(s):

    queue = deque(s)


    while True:
        chk = False
        new_queue = deque([])
        while len(queue) > 1:

            ch1 = queue.popleft()

            if ch1 == queue[0]:
                queue.popleft()
                while new_queue and queue:
                    if new_queue[len(new_queue)-1] == queue[0]:
                        new_queue.pop()
                        queue.popleft()
                    else:
                        break

                chk = True
            else:
                new_queue.append(ch1)


        if chk == False:
            return 0
        elif not queue and not new_queue:
            return 1
        else:
            new_queue.append(queue.popleft)
            queue = new_queue.copy()

def solution2(s):
    stack = deque([])
    idx = 0
    while idx < len(s):
        if not stack:
            stack.append(s[idx])
            idx += 1
        else:
            while stack and idx < len(s):
                if s[idx] == stack[len(stack)-1]:
                    stack.pop()
                    idx += 1
                else:
                    stack.append(s[idx])
                    idx += 1
    if not stack:
        return 1
    else:
        return 0

a = "a1acacbbca"
print(solution2(a))
