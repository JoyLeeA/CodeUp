h, w = map(int, input().split())
n = int(input())
# d -> 가로=0 세로=1
board = [[0] * w for _ in range(h)]
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d: #세로
        for i in range(l):
            board[x-1+i][y-1] = 1
    else: #가로
        for i in range(l):
            board[x-1][y-1+i] = 1

for i in range(h):
    print(*board[i])
