N = int(input())
result = 0
for i in range(1,N+1):
    if not i%2:
        result += i
print(result)