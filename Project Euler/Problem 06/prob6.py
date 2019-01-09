suma = 0
sumb = 0
n = int(input())
for i in range(1,n+1):
    suma += i**2
    sumb += i
sum = sumb**2 - suma
print(sum)
