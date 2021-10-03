# sum of squares of first n natural numbers

n = int(input("enter the range:"))
sum = 0

for num in range(1,n+1): 
    a = num**3
    sum += a

print(sum)
