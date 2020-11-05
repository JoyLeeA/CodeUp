N = int(input())
board = [[0]*19 for _ in range(19)]
for _ in range(N):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

for i in range(19):
    print(*board[i])