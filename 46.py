N, M = map(int, input().split())

if M-1 < 0:
    K = 1
else:
    K = 2<<(M-1)
print(N*K)

# a,b=input().split()

# x=int(a)
# y=int(b)

# print(x<<y)