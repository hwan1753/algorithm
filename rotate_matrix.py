def rotate(board): # 시계방향
    return [list(reversed(p)) for p in zip(*board)]
def rotate(board): # 반시계방향
    return [list(p) for p in zip(*board)][::-1]