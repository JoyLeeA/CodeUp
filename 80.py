N = input()
Num = int(N,16)
for i in range(1,16):
    print('{:X}*{:X}={:X}'.format(Num, i, Num*i))