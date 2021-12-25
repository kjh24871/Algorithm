import math

def solution():
    a,b,c = input().split()

    if int(b) >= int(c):
        print(-1)
    else:
        num = int(a)/(int(c)-int(b))
        print(math.floor(num+1))


solution()