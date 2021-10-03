# withot any input
# num =15
#with input 
num = int(input("enter a number: \n"))

#main logic

for i in range(1,num+1):
    if (i % 3 == 0) and (i % 5 == 0) :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

