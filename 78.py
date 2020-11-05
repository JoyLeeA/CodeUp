N = int(input())
i = 1
result = 0
while True:
    result += i
    if result >= N:
        print(i)
        break
    i += 1