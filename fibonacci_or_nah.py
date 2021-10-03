n = int(input("Enter the number you want to check: "))
 
# variables for generating fibonacci sequence
f3 = 0
f1 = 1
f2 = 1
# 0 and 1 both are fibonacci numbers
if (n == 0 or n == 1):
    print("Given number is fibonacci number")
 
else:
    # generating the fibonacci numbers until the generated number is less than  n
    while f3 < n:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == n:
        print("Given number is fibonacci number")
    else:
        print("no it’s not a fibonacci number")