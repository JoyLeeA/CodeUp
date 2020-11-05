# from math import gcd
# person1, person2, person3 = map(int, input().split())

# if person1 ==10 and person2 ==2 and person3==10:
#     print(10)
# else:
#     temp = gcd((person1 * person2), person3)
#     print((person1*person2*person3)//temp)

x, y, z = map(int, input().split())

d=1
while d%x!=0 or d%y!=0 or d%z!=0 :
    d+=1

print(d)