N = int(input())
for i in range(1,N+1):
    if not i%3:
        print('X', end=' ')
    else:
        print(i, end=' ')
print()