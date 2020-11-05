board = [list(map(int, input().split())) for _ in range(19)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(19):
        if board[x-1][i]:
            board[x-1][i] = 0
        else:
            board[x-1][i] = 1
    for j in range(19):
        if board[j][y-1]:
            board[j][y-1] = 0
        else:
            board[j][y-1] = 1

for k in range(19):
    print(*board[k])