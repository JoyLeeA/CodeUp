def move(x,y):
    if arr[x][y+1] =='1': 
        if arr[x+1][y] == '1':
            return # 아래 오른쪽이 벽이면 멈춤.
        else : 
            if arr[x+1][y] == '2': 
                arr[x+1][y] ='9'
                return #아래에 먹이가 있으면 이동후 종료.
            else:
                arr[x+1][y] = '9' 
                move(x+1,y) #아래에 먹이 없으면 이동후 재귀.
    else: #오른쪽이 벽이 아니면
        if arr[x][y+1] == '2':
            arr[x][y+1] = '9'
            return #오른쪽에 먹이 확인 후 있으면 이동후 종료.
        else:
            arr[x][y+1] ='9'
            move(x,y+1) #먹이없으면 오른쪽으로 이동.

arr = [[0]*10 for i in range(10)]

for i in range(10):
    a = input().split()
    arr[i] = a
arr[1][1] = '9'
move(1,1)

for i in range(10):
    for j in range(10):
        print(arr[i][j],end= ' ')
    print()