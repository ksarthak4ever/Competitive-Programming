n=int(input())
prime=1
i=2
while(i*i<=n):
    while(n%i==0):
        prime=i
        n/=i
    i+=1
if(n>1):
    prime=int(n)
print(prime)
