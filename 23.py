N = input()
temp = 0
for idx, i in enumerate(N):
    temp = i + ('0'*(4-idx))
    print('[{}]'.format(temp))