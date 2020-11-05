w, h, b = map(int, input().split())
bit = (w * h * b) / 8
KB = bit / 1024
MB = round(KB / 1024, 2)
print('{:.2f} MB'.format(MB))