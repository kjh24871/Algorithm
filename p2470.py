def solution():
    n = int(input())
    num = input().split()
    temp=0
    flag=2000000000

    answer0=0
    answer1=0
    num.sort(key = lambda x: (abs(int(x))))

    for i in range(len(num)-1):
        temp = int(num[i]) + int(num[i+1])
        if abs(flag) >= abs(temp):
            flag = temp
            answer0 = int(num[i])
            answer1 = int(num[i+1])
    if answer0 >= answer1:
        print(answer1, end=" ")
        print(answer0)
    else:
        print(answer0, end=" ")
        print(answer1)


solution()
