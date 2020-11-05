N = int(input())
data = list(map(int, input().split()))
result = [0] * 23
for i in data:
    result[i-1] += 1

print(*result)