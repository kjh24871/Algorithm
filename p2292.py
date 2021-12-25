def solution():
    a = int(input())
    count=1
    total=1
    if a==1:
        print(1)
    else:
        while True:
            total+=6*count
            count+=1
            if total>=a:
                break
        print(count)

solution()