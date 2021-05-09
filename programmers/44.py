from _collections import deque
from pprint import pprint
import heapq


from _collections import deque

def solution(n, start, end, roads, traps):
    answer = 0
    trap_arr = [0]*(n+1)
    for t in traps:
        trap_arr[t] = 1
    # node_dict = {i:[] for i in range(1,n+1)}
    # reverse_dict = {i:[] for i in range(1,n+1)}
    # for P, Q, S in roads:
    #     node_dict[P].append((Q,S))
    #     if P in traps or Q in traps:
    #         # reverse_dict[P].append((Q,S))
    #         reverse_dict[Q].append((P,S))
    board = [[1e9]*(n+1) for _ in range(n+1)]
    for P,Q,S in roads:
        board[P][Q] = min(S, board[P][Q])


    visit = deque([(start,0)])
    dp = [1e9]*(n+1)
    dp[start] = 0

    while visit:

        now, weight = visit.popleft()

        for next_node, plus in enumerate(board[now]):
            if plus != 1e9 and (0<trap_arr[next_node]<3 or weight + plus < dp[next_node]):
                visit.append((next_node, weight+plus))
                dp[next_node] = weight+plus
                if trap_arr[next_node]:
                    trap_arr[next_node] += 1
                    for i in range(n+1):
                        if board[i][next_node] == 0 and board[next_node][i] == 0:
                            continue

                        board[next_node][i], board[i][next_node] = board[i][next_node], board[next_node][i]

        # print(visit)
        # print(dp)
    return dp[end]


a1 = 4
a2 = 1
a3 = 4
a4 = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
a5 = [2,3]
print(solution(a1,a2,a3,a4,a5))

# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 1
# 0 0 1 0 0
# 0 0 0 0 0

# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# 0 0 1 0 0