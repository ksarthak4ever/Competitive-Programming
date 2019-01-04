t=int(input().strip()) #Inputing Number of Test Cases
for i in range (1,t+1):
    n = int(input().strip()) #Inputting Range or value of N 
    sum=0
    for a in range(3,n):
        if(a%3==0 or a%5==0):
            sum+=a
    print(sum)
