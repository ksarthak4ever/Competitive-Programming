arr = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        t = str(i*j)
        if t == t[::-1]:
            arr.append(i*j)
arr.sort()

n=int(input())
for i in arr[::-1]:
    if(i<n):
        print(i)
        exit(0)
