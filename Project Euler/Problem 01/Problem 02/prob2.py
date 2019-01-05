import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=1
    j=2 
    sum=0
    while(j<=n):
        if((j%2)==0): 
            sum+=j
        temp=i
        i=j
        j=temp+i
    print(sum)