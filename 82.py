R, G, B = map(int, input().split())

cnt = 0
for i in range(R):
    for j in range(G):
        for l in range(B):
            print(i, j, l)
            cnt += 1
print(cnt)

