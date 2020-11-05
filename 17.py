# year, month, day = input().split('.')
# if len(year) < 3:
#     year = "00" + year
# if len(month) < 2:
#     month = '0'+ month
# if len(day) < 2:
#     day = '0' + day

# print('{}.{}.{}'.format(year,month,day))

year, month, day = map(int,input().split('.'))
print('{:04d}.{:02d}.{:02d}'.format(year,month,day))
