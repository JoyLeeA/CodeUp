# 0:갈수 있는 곳 1:벽 또는 장애물 2:먹이
# 개미는 (2,2)에서 출발 9:이동경로
maze = [ list(map(int, input().split())) for _ in range(10)]
x = y = 1

flag = True
if maze[y][x] == 2:
    flag = False
maze[y][x] = 9

while flag:
    if maze[y][x+1]==0:
        maze[y][x+1] = 9
        x += 1
    elif maze[y][x+1]==1 and maze[y+1][x]==0:
        maze[y+1][x] = 9
        y += 1        
    elif maze[y][x+1] == 1 and maze[y+1][x]==2:
        maze[y+1][x] = 9
        break
    elif maze[y][x+1]==2:
        maze[y][x+1] = 9
        break
    else:
        break

for i in range(10):
    print(*maze[i])
