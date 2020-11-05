h, b, c, s = map(int, input().split())
bit = (h * b * c * s)/8
KB = bit/1024
MB = round(KB/1024, 1)
print('{} MB'.format(MB))
