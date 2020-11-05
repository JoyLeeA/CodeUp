N = int(input())
result = 0
i = 1
while True:
    result += i
    if result >= N:
        print(result)
        break
    i += 1